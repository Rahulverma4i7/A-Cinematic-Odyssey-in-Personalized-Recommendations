import streamlit as st

st.image('projecttop.svg', use_column_width=True)
def project_page():
    st.title('Our Projects')

    projects = [
        {
            'name': 'React Web Application',
            'description': 'React Web Chat Application: This project involves building a chat application using React for the front end, PHP for server-side scripting, HTML and CSS for design, MySQL for database management, and AJAX for asynchronous communication. It allows users to communicate in real-time via text messages over the internet.',
            'image': 'chat1.svg',
            'github_link': 'https://github.com/Rahulverma4i7/ChatApp_with_dashboard'
        },
        {
            'name': 'False Message Detection',
            'description': 'False Message Detection: This project focuses on developing a system to detect false messages using Python. It utilizes an Artificial Neural Network (ANN) model, a type of machine learning algorithm, to analyze message content and identify false or misleading information. The system aims to improve the accuracy of identifying deceptive messages in various contexts.',
            'image': 'false1.svg',
            'github_link': 'https://github.com/Rahulverma4i7/False_message_detection'
        },
        {
            'name': 'React Admin Dashboard',
            'description': 'React Admin Dashboard: This project aims to create an admin dashboard using React, a JavaScript library for building user interfaces, and Material-UI, a popular React UI framework that implements Google Material Design. The dashboard provides a visual interface for administrators to manage and monitor various aspects of a web application, such as user accounts, content, and settings.',
            'image': 'dashboard1.svg',
            'github_link': 'https://github.com/Rahulverma4i7/react_master_dash'
        }
    ]

    for project in projects:
        st.write(f"## {project['name']}")
        st.image(project['image'], use_column_width=True)
        st.write(project['description'])
        st.markdown(f"GitHub: [{project['name']}]({project['github_link']})")
        st.write('---')

project_page()
