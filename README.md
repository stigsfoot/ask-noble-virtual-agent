# Ask Noble | Virtual Agent

## Overview

This Streamlit application serves as a virtual assistant, leveraging Retrieval Augmented Generation (RAG) and the LlamaIndex library to provide accurate and insightful information based on indexed documents. It's designed to mirror Noble Ackerson's expertise in emergent technologies, product strategy, and related subjects.

## Features

- Factually accurate responses using RAG
- Multiple data handling options (e.g., MongoDB, SimpleDirectory)
- Modular, scalable, and designed for enterprise-grade deployment

## Prerequisites

- Python 3.x
- Streamlit
- LlamaIndex library
- MongoDB (Optional)

## Installation

1. Clone the repository.
    ```
    git clone https://github.com/stigsfoot/ask-noble-virtual-agent.git
    ```

2. Navigate to the project directory.
    ```
    cd ask-noble-virtual-agent
    ```

3. Install the required packages.
    ```
    pip install -r requirements.txt
    ```

## Configuration

- The `config_helper.py` file is used for setting up the Streamlit app's initial configurations.
- Data handlers are implemented in `data_handlers.py`.
- The factory pattern is implemented in `data_handler_factory.py` for future scalability in adding new data handlers.
- The `readers.py` file is used for different reader classes.

## Usage

1. Start the Streamlit app.
    ```
    streamlit run streamlit_app.py
    ```

2. Select the data handler you wish to use from the dropdown.
3. Interact with the virtual assistant.

## Troubleshooting

If you encounter any issues, check the following:

- Make sure all dependencies are installed.
- Ensure MongoDB is running if you are using it as a data handler.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss the change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
