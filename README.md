![Static Badge](https://img.shields.io/badge/Project_Status-Complete-brightgreen) ![Static Badge](https://img.shields.io/badge/Build-Passing-brightgreen) ![Static Badge](https://img.shields.io/badge/Open_to_Collaboration-Yes-orange)

<h1> Project: News Update using API Services </h1>

This program demonstrates how to extract real-time news updates using API services. 
It connects to various news sources, retrieves relevant data, and compiles a concise summary. 
The extracted news is then delivered via email to subscribers.

<h3> Table of Contents </h3>

- System Details
- Installation
- Usage
- Screenshots
- Features
- Licence
- Authors and acknowledgment

<h3> System Details </h3>

- **Language:** Built with Python 3.12.
- **Development Environment:** Developed using PyCharm IDE.
- **Version Control:** Managed with Git.

<h3> Installation </h3>

* Clone the repository:
    ```bash
    git clone https://github.com/davedepo/app5a-newsapi-email.git
    ```
* Install dependencies: 
    ```bash
    pip install -r requirements.txt
    ```

<h3> Usage </h3>
 
**A. To connect to API services & extract news, run;**

   - Ideal for users familiar with running Python programs
      ```
      newsAPIemail.py
      ```
     OR

      ```
      testAPIemail.py
      ```

**B. To run or host this program as a scheduled task;**

   - Ideal for users familiar with cloud hosting services:
   1. Deploy the program on a cloud service (such as PythonAnywhere or Heroku).
   2. Configure a scheduled trigger to run the program at specific intervals (daily, hourly, etc.).

<h3> Screenshots </h3>

   ![test API email](/app_screenprint/testAPIemail.png?raw=true "sample")

<h3> Features </h3>

This Minimum Viable Product (MVP) focuses on automating a daily news digest delivery system. Here's a breakdown of its core functionalities:

- API Integration: Leverages APIs from reputable news sources to retrieve fresh and relevant news data.
- Efficient Data Processing: Seamlessly gathers and processes news updates to ensure a smooth user experience.
- Automated Email Delivery: Delivers personalized daily news summaries directly to subscribers' inboxes.

It showcases the power of APIs in data acquisition and streamlines the news consumption process. It offers a strong foundation to expand upon based on specific requirements. Potential future enhancements include:

- Interactive Interface: Develop a user-friendly interface (e.g., using Streamlit) to allow customization of news topics and preferred delivery frequency.
- Advanced Features: Integrate features like sentiment analysis to provide insights into the overall tone of the news or topic categorization for targeted delivery.

<h3> Licence </h3>

This project is licensed under the MIT License.

<h3> Authors and Acknowledgment </h3>

- **Udemy**: For providing a platform to learn.
- **Ardit Sulce** (https://github.com/arditsulceteaching) : Created a code-along learning module for building this app.
- **Python Developers & Community**: Provided extensive documentation and examples to support this learning.
- **OpenAI and Copilot**: For providing support, assistance, and encouragement in this learning journey.
- **PyCharm Team:** Making it easy to learn with all embedded features for beginners.
