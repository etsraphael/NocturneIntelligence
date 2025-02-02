# Nocturne Intelligence – Stock Trading Bot

**Nocturne Intelligence** is a long-term project that aims to create a cutting-edge, intelligent chatbot to assist users in making informed decisions about stock trading. This repository hosts the codebase and documentation for Nocturne Intelligence’s stock trading companion, providing features ranging from real-time market insights to automated trade execution and portfolio management.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Roadmap](#roadmap)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Disclaimer and Liability](#disclaimer-and-liability)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

---

## Introduction
Nocturne Intelligence is envisioned to become an **all-in-one personal trading assistant** for both novice and experienced traders. By leveraging AI-driven insights and robust data processing, Nocturne Intelligence can help users:

- Research and analyze financial markets
- Explore real-time market data
- Identify potential trading opportunities
- Execute and manage trades (planned for future releases)

The ultimate goal is to create a comprehensive, user-friendly system that not only demystifies the stock market, but also supports users in building long-term wealth and financial resilience.

---

## Features
**Current and Planned Features** include:

1. **Market Data Integration**
   - Pull live market data for equities and indices
   - Retrieve historical data for in-depth analysis
   - Streamline data collection and storage

2. **Technical and Fundamental Analysis**
   - Generate technical indicators (EMA, MACD, RSI, etc.)
   - Provide sentiment analysis based on news or social media feeds
   - Offer basic fundamental metrics (P/E ratio, earnings history, etc.)

3. **Portfolio Tracking**
   - Monitor user’s portfolio performance
   - Compare current holdings against major benchmarks
   - Provide daily/weekly summary reports

4. **Trade Simulation**
   - Simulate stock trades on virtual paper-trading environments
   - Help novices practice trading strategies without real capital at risk

5. **Automated Trading (Future Roadmap)**
   - Implement trade execution via broker APIs
   - Set up algorithmic or rules-based trading strategies
   - Configure stop-loss and take-profit triggers

6. **User-Friendly Interface**
   - Interactive chat-based UI for guidance and Q&A
   - Dashboard with real-time analytics and alerts
   - Customizable notifications via email or chat platforms

---

## Roadmap
Nocturne Intelligence is a long-term effort with multiple development phases:

1. **Data Collection & Analysis (Current Focus)**
   - Ensure real-time and historical data reliability
   - Establish robust frameworks for technical and fundamental analysis

2. **Enhanced Trading Logic & Strategy Research**
   - Implement advanced AI algorithms for pattern recognition
   - Develop experimental quantitative trading strategies

3. **User Interface & Experience**
   - Build an engaging, intuitive interface
   - Incorporate user feedback to refine UX and workflows

4. **Automated Trading & Portfolio Management**
   - Integrate broker APIs to enable live trade execution
   - Provide advanced features such as auto-hedging, risk metrics, and performance optimization

5. **Regulatory Compliance & Security**
   - Work towards ensuring compliance with relevant trading rules and regulations
   - Incorporate robust security measures and best practices

6. **Scaling & Distributed Architecture**
   - Optimize server and database infrastructure for large volumes of user requests
   - Implement distributed processing for real-time data feeds

Each milestone is designed to build upon the previous one, ensuring a systematic and reliable approach toward a fully-fledged AI-driven trading assistant.

---

## Progress Update

Recent developments in Nocturne Intelligence:
- Implemented new technical indicator modules (e.g., DJIAWeakness in src/indicators/djia_weakness.py).
- Improved stock data cleaning and validation in get_stock_data.py for accurate data analysis.
- Integrated indicator processing with indicator data outputs in get_indicator_data.py.
- Enhanced data visualization capabilities in create_graph.py for better trend analysis.
- Continued roadmap progress towards a full-featured trading assistant.

---

## Installation

To install and run Nocturne Intelligence locally, follow the steps below:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/etsraphael/NocturneIntelligence.git
   cd NocturneIntelligence
   ```

2. **Set Up Virtual Environment (Optional but Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   - Create a file named `.env` in the project root to store your environment variables (e.g., API keys for market data, broker credentials, etc.).
   - See [Configuration](#configuration) for details.

5. **Run the Bot**
   ```bash
   python run_nocturne.py
   ```
   This command will launch Nocturne Intelligence in your terminal (or a web interface, depending on your setup).

---

## Usage

### 1. Interactive Mode
After running `python run_nocturne.py`, you can interact with the bot via a command-line interface. Type your questions or commands, and Nocturne Intelligence will respond accordingly.

Example commands:
- `show market data for AAPL`
- `analyze RSI for TSLA`
- `simulate a $10,000 trade on AMZN`
- `show my portfolio performance`

### 2. Web Dashboard (Future Release)
A web-based dashboard will be introduced in a future version. This will allow you to:
- Access real-time analytics from any device
- Manage your portfolio in a visual interface
- Configure automated trading parameters through a secure portal

### 3. API Integration
For advanced users and developers, Nocturne Intelligence will offer an API for integrating with existing systems or workflows. This API will provide endpoints for:
- Account and portfolio information
- Trading signals and alerts
- Execution commands (pending broker integration)

---

## Disclaimer and Liability

> **Important**: Nocturne Intelligence is a **research and educational tool** meant to guide and assist users in understanding financial markets. It does **not** guarantee any profits or the prevention of losses. While we make every effort to provide accurate information and reliable functionality, **use the system at your own risk**.

- Stock trading and investing involve **significant risk** of loss.
- Past performance of any strategy does not guarantee future results.
- Always consult with a qualified financial advisor or conduct thorough personal research before making investment decisions.
- The maintainers and contributors of Nocturne Intelligence **will not be held liable** for any financial losses or damages resulting from the use of this software.

---

## Contributing

We welcome contributions from developers, data scientists, and domain experts. To contribute:

1. **Fork the Repository** – Create a personal fork of this project.
2. **Create a Feature Branch** – Work on your changes in a dedicated branch.
3. **Test Thoroughly** – Ensure your modifications pass all tests.
4. **Submit a Pull Request** – Open a pull request detailing your changes and rationale.

For major changes, please open an issue first to discuss your proposed modifications. This helps prevent duplication of work and ensures alignment with the project roadmap.


## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details. Under this license, you’re free to use, modify, and distribute Nocturne Intelligence’s code. However, the maintainers are not responsible for any misuse or damage caused by this software.

---

## Contact

**My IG:** [https://www.instagram.com/rafael.salei/](https://www.instagram.com/rafael.salei/)

---

*Thank you for your interest in Nocturne Intelligence. We look forward to building a powerful, transparent, and innovative trading assistant that helps users confidently navigate the stock market.*
