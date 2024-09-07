

---

# Startup Dashboard

Welcome to the **Startup Dashboard**! This Streamlit application offers an in-depth analysis of startup funding data, providing users with various metrics and visualizations to explore investments, sectors, and investor activities.

Explore the live dashboard: [Startup Dashboard](https://startupfunding2010s.streamlit.app/)

## Features

- **Overall Analysis**: Gain insights into total funding, maximum funding, average funding, and the number of funded startups. View month-on-month funding trends, top sectors, funding types, city-wise funding, top startups, and a funding heatmap.
- **Startup Analysis**: Delve into individual startups, including details about their industry, sub-industry, location, and funding rounds.
- **Investor Analysis**: Explore information about specific investors, including recent investments, top investments, investment verticals, and round details. Review year-on-year investment trends for each investor.

## Installation

To run this application, ensure you have Python and the necessary libraries installed. Follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Dependencies**:
    ```bash
    pip install streamlit numpy pandas matplotlib seaborn plotly
    ```

3. **Download the Dataset**:
    Ensure the `startup_clean.csv` file is located in the same directory as `app.py`. The dataset should include the following columns:
    - `startup`: Name of the startup
    - `amount`: Funding amount
    - `date`: Date of investment
    - `investors`: Names of investors
    - `vertical`: Industry sector
    - `subvertical`: Sub-industry sector
    - `city`: City of the startup
    - `round`: Funding round

## Usage

1. **Run the Streamlit Application**:
    ```bash
    streamlit run app.py
    ```

2. **Interact with the Dashboard**:
    - **Sidebar**: Choose the analysis type you wish to view (Overall Analysis, Startup, or Investors).
    - **Overall Analysis**: Click "Show Overall Analysis" to view metrics, trends, and charts related to the overall funding data.
    - **Startup Analysis**: Select a startup from the sidebar and click "Show Startup Analysis" to see detailed information about the chosen startup.
    - **Investor Analysis**: Choose an investor from the sidebar and click "Find Investor Details" to explore their investment details.

## Features and Visualizations

- **Metrics**: Key statistics such as total funding, maximum funding, average funding, and the number of funded startups.
- **Month-on-Month Funding Analysis**: Line chart illustrating funding trends over time.
- **Top Sectors**: Pie chart displaying the most funded sectors.
- **Funding Type Distribution**: Bar chart showing the distribution of different funding rounds.
- **City-wise Funding**: Bar chart representing funding amounts by city.
- **Top Startups**: Pie and bar charts showcasing the top startups by funding amount.
- **Funding Heatmap**: Heatmap showing the distribution of funding amounts across different years and funding rounds.
- **Startup Details**: Detailed view of a specific startup’s industry, sub-industry, location, and funding rounds.
- **Investor Details**: Insights into an investor’s recent investments, top investments, investment verticals, and round details, along with year-on-year investment trends.

## Contributing

Contributions are welcome! To contribute to this project, please follow these guidelines:

1. **Fork the Repository** and create a new branch.
2. **Make Your Changes** and commit them with clear, descriptive messages.
3. **Push Your Changes** to your forked repository.
4. **Create a Pull Request** with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).

---

Feel free to adjust any details or add specific information as needed for your project.
