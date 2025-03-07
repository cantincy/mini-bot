import streamlit as st
from langchain.chains.llm import LLMChain
from langchain.memory import VectorStoreRetrieverMemory
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

persist_directory = "./chroma_db"


# 缓存 LLM 对象避免重复创建
@st.cache_resource
def load_llm():
    return ChatOpenAI()


# 缓存 Chain 对象（包含固定模板）
@st.cache_resource
def create_chain():
    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=OpenAIEmbeddings()
    )

    retriever = vector_store.as_retriever()

    memory = VectorStoreRetrieverMemory(
        retriever=retriever,
        memory_key="history",
        return_docs=True
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", """
        你是一个专业的问答助手，请借助历史上下文回答问题。
        历史上下文如下：
        ```
        {history}
        ```
        """),
        ("human", "{input}")
    ])

    chain = LLMChain(
        llm=load_llm(),
        prompt=prompt,
        memory=memory,
        verbose=True
    )

    return chain


def main():
    st.subheader("智能问答助手")
    st.write("您可以上传txt文档，我们将为您生成摘要。")

    # 从缓存获取已初始化的对象
    chain = create_chain()

    question = st.chat_input()
    file = st.file_uploader("上传文档", type=["txt"])

    if question:
        res = chain.invoke({"input": question})
        st.markdown(res["text"])

    elif file:
        data = file.read().decode('utf-8')

        question = f"""
                ```中包含的是一个文档的内容，请根据文档的内容生成摘要，摘要的内容应该包括文档的主要内容。
                文档：
                ```
                {data}
                ```
                """

        res = chain.invoke({"input": question})
        st.markdown(res["text"])


if __name__ == '__main__':
    main()
