# 智能问答助手 - minibot

这是一个基于 Streamlit 和 LangChain 构建的智能问答助手应用。用户可以通过上传文本文档或直接提问，应用会生成相应的摘要或回答问题。

## 功能介绍

- **文档摘要生成**：用户可以上传 `.txt` 文件，应用会根据文档内容生成摘要。
- **智能问答**：用户可以直接输入问题，应用会基于历史上下文和上传的文档内容回答问题。

## 技术栈

- **Streamlit**：用于构建交互式 Web 应用。
- **LangChain**：用于构建和管理语言模型链。
- **OpenAI**：用于提供语言模型（ChatGPT）和嵌入模型。
- **Chroma**：用于存储和检索向量化的历史上下文。

## 安装与运行

1. **克隆仓库**
```
git clone https://github.com/your-repo/your-project.git
cd your-project
```
2. **安装依赖**

```
pip install -r requirements.txt
```

3. **设置 OpenAI API 密钥**

在运行应用之前，请确保已设置 OPENAI_API_KEY 和 环境变量。

4. **运行应用**

```
streamlit run app.py
```