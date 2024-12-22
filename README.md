# Homework

---

## **Pre-requisites**

Before running the test, ensure the following are installed and configured:

- **Python 3.10.6**
- **Google Chrome** browser
- **ChromeDriver** (compatible with your Chrome version) - install using: `brew install chromedriver --cask`
- **Selenium**, **Pytest**, **python-dotenv** Python libraries

To install the required Python libraries, use the following command:
```bash
pip install -r requirements.txt
```

---

## **Setup Instructions**

1. Clone this repository.
2. Navigate to the project directory.
3. Edit the .env file to specify your ChromeDriver location.

---

## **How to Run the Test**

To execute the test, use the following command:
```bash
pytest tests/test_twitch_search.py
```

### **Output:**
- A screenshot will be saved in the project directory as `streamer_page.png` after the streamer page loads successfully.

---

## **Framework Structure**

```plaintext
tino_hw_2/
├── pages/                          # Page objects for twitch
├── tests/
│   ├── test_twitch_search.py       # Test case implementation
├── utils/
│   ├── browser_setup.py            # Browser configuration setup
├── conftest.py                     # Entry point of pytest
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
└── .env                            # Files to set environments
```

---

## GIF

![result](https://github.com/TinoChen105/tino_hw_2/blob/main/result.gif)

