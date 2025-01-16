# NostrBrainAddressGenerator / Nostr脑地址生成器

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**English | [中文](#中文)**

## Introduction

`NostrBrainAddressGenerator` is a simple, open-source tool for generating Nostr private and public keys using a brain wallet approach. It allows you to derive multiple Nostr identities from a single passphrase, enhancing security through salting and multiple hashing iterations.

**Disclaimer:** This tool is for educational and informational purposes. Please use it responsibly and understand the security implications of brain wallets.

## Features

*   Generates Nostr private and public key pairs based on a passphrase, salt, and number of hash iterations.
*   Allows specifying the number of key pairs to generate.
*   Provides a user-friendly GUI interface.
*   Displays the initial passphrase hex encoding, the final SHA-256 hash, and a list of private and public keys.
*   Copies generated keys to the clipboard.
*   No longer generates BIP39 Mnemonic Words
*   The generated keys are not compatible with Bitcoin or other cryptocurrency addresses. It's only for Nostr.

## How to Use

1.  **Prerequisites:**
    *   Python 3.7 or higher
    *   `pynostr` library
2.  **Installation:**
    *   Install the required packages by running `pip install -r requirements.txt`
3.  **Run the Application:**
    *   Execute the main script with `python <script_name>.py`
4.  **Usage:**
    *   Enter your passphrase in the "Passphrase" field.
    *   Optionally enter a salt in the "Salt" field.
    *   Enter the number of hash iterations in the "Hash Times" field (1-10000).
    *   Enter the number of key pairs you want to generate in the "Generate Count" field (1-1000).
    *   Click the "Generate Nostr Keys" button to generate your Nostr keys.
    *   The generated keys will be displayed in the result area below.
    *   Click the "Copy Nostr Keys" button to copy the result to the clipboard.
    *   Click the "Clear All" button to clear all input and output.

## Security Warning

*   Brain wallets can be vulnerable if your passphrase is not strong enough.
*   Use a long, random, and unique passphrase to generate your keys.
*   Salting and multiple hashing iterations are used to increase security, but it doesn't eliminate all risks.
*   **This tool is provided as-is without any warranty. Use it at your own risk.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit pull requests, report bugs, and suggest new features.

---

<a id="中文"></a>
## 中文

## 介绍

`NostrBrainAddressGenerator` 是一个简单的开源工具，用于使用脑钱包方法生成 Nostr 私钥和公钥。 它允许你从单个密码派生多个 Nostr 身份，并通过加盐和多次哈希迭代来增强安全性。

**免责声明：** 此工具仅用于教育和信息目的。请负责任地使用它，并理解脑钱包的安全性含义。

## 特性

*   基于密码，盐和哈希迭代次数生成 Nostr 私钥和公钥对。
*   允许指定要生成的密钥对数量。
*   提供用户友好的GUI界面。
*   显示初始密码的十六进制编码，最终SHA-256哈希以及私钥和公钥列表。
*   将生成的密钥复制到剪贴板。
*    不再生成 BIP39 助记词
*   生成的密钥与比特币或其他加密货币地址不兼容。它仅适用于 Nostr。

## 如何使用

1.  **先决条件：**
    *   Python 3.7或更高版本
    *   `pynostr` 库
2.  **安装：**
    *   通过运行 `pip install -r requirements.txt` 安装所需的软件包
3.  **运行应用程序：**
    *   使用 `python <脚本名称>.py` 执行主脚本
4.  **用法：**
    *   在“密码”字段中输入你的密码。
    *   （可选）在“盐”字段中输入盐。
    *   在“哈希次数”字段中输入哈希迭代次数 (1-10000).
    *   在“生成数量”字段中输入要生成的密钥对数 (1-1000).
    *   点击“生成 Nostr 密钥”按钮以生成你的 Nostr 密钥。
    *   生成的密钥将显示在下方的结果区域中。
    *   点击“复制 Nostr 密钥”按钮将结果复制到剪贴板。
    *   点击“全部清除”按钮清除所有输入和输出。

## 安全警告

*   如果你的密码不够强，则脑钱包可能很脆弱。
*   使用长，随机且唯一的密码来生成你的密钥。
*   使用加盐和多次哈希迭代可以提高安全性，但并不能消除所有风险。
*   **此工具按原样提供，不提供任何担保。请自行承担使用风险。**

## 许可证

该项目在 MIT 许可证下获得许可 - 有关详细信息，请参见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交拉取请求、报告错误并建议新功能。
