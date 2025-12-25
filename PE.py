import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw  #image editing
import login #database functions
import space1w
import space2w
import space3w

st.set_page_config(page_title="Parkease",page_icon=":parking:",layout="wide")

# color 
#455262

import base64

# Convert local image to base64 for embedding inside the box
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Replace with your local image path
image_path = "parkeasename.jpg"  # Ensure this file exists in the same directory
image_base64 = get_base64_image(image_path)

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Function to change the page
def navigate_to(page):
    st.session_state.current_page = page

# Inject CSS for the blurred GIF background and box
st.markdown("""
    <hr style="border: none; height: 4px; background-color: #455262; margin: 20px 0;">
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6 = st.columns([1,2,1,1,1,1])
with col1:
    st.image(image_path)
# with col2:
    
with col3:
    if st.button("Home",type="tertiary"):
        navigate_to("home")
with col4:
    if st.button("Sign Up",type="tertiary"):
        navigate_to("signup")
with col5:
    if st.button("Login",type="tertiary"):
        navigate_to("login")
with col6:
    if st.button("Profile",type="tertiary"):
        navigate_to("profile")
        st.session_state.current_page = "profile"
st.markdown("""
    <hr style="border: none; height: 4px; background-color: #455262; margin: 0px 0;">
""", unsafe_allow_html=True)


# Render content based on current page

if st.session_state.current_page == "home":

# css videooo

    def park_action():
        navigate_to("signup")

    with open("blurcarparkgif.mp4", "rb") as f:
        video_base64 = base64.b64encode(f.read()).decode('utf-8')

# Show the video with text
    st.markdown(f"""
    <style>
    .stApp {{
        background: transparent;
    }}
    .video-container {{
        position: relative;
        width: 100%;
        height: 100vh;
        overflow: hidden;
    }}
    #bgvid {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: -1;
        padding-bottom:20px;
    }}
    .text-overlay {{
        position: absolute;
        top: 65%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(0, 0, 0, 0.7);
        padding: 20px ;
        border-radius: 20px;
        text-align: center;
        width: 70%
        
    }}
    .text-overlay h1 {{
        color: white;
        font-size: 26px;
        margin: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    </style>

    <div class="video-container">
        <video autoplay muted loop playsinline id="bgvid">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        <div class="text-overlay">
            <h1>PARKEASE: Drive less, park smarter — saving time, slashing emissions, and shaping smarter cities.</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Centered button in Streamlit
    col1, col2, col3 = st.columns([0.5, 1, 0.5])
    with col2:
        if st.button("Let's Park",use_container_width=True):
            park_action()

    # why us?
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; padding-top: 50px;">
        <h1 style="
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 36px;
            bold: no;
            color: #184676;
            text-align: center;
            margin: 0;
        ">
            WHY US?
        </h1>
    </div>
""", unsafe_allow_html=True)
    
    # 3 COLUMNS CONTAINERS 
    col1, col2,col3 = st.columns([1,1,1])

    # feature1
    with col1:

        
        st.markdown("""
    <div style="
        width: 100%; 
        margin:  auto; 
        background-color: #e6f2ff; 
        padding: 60px; 
        padding-bottom: 95px; 
        border-radius: 12px; 
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
        text-align: center; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
        color: #333333; 
        font-size: 18px; 
        line-height: 1.4;
    ">  
                    <h3 style="color: #003366; margin-bottom: 10px;">Real-Time Space Availability</h3>
                    ParkEase provides live updates on open parking spots, saving you time and frustration.
    </div>
""", unsafe_allow_html=True)
        

    with col2:

        
        st.markdown("""
    <div style="
        width: 100%; 
        margin: auto; 
        background-color: #e6f2ff; 
        padding: 60px; 
        border-radius: 12px; 
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
        text-align: center; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
        color: #333333; 
        font-size: 18px; 
        line-height: 1.4;
    ">  
                    <h3 style="color: #003366; margin-bottom: 10px;">Eco-Friendly Parking Optimization</h3>
                    By minimizing search time, ParkEase helps cut down on traffic congestion and pollution.
    </div>
""", unsafe_allow_html=True)
        

    with col3:

        
        st.markdown("""
    <div style="
        width: 100%; 
        margin: auto; 
        background-color: #e6f2ff; 
        padding: 60px;
        padding-bottom: 95px; 
        border-radius: 12px; 
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
        text-align: center; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
        color: #333333; 
        font-size: 18px; 
        line-height: 1.4;
    ">  
                    <h3 style="color: #003366; margin-bottom: 10px;">Urban Planning Insights</h3>
                    Aggregated data supports city planners to create more efficient, sustainable urban spaces.
    </div>
""", unsafe_allow_html=True)
    
# CONTACT US
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f6ff;
        }
        .contact-container {
            width: 100%;
            min-height: 10vh;
            background-color: #f5f6ff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 10px 10px;
            
        }
        .contact-header {
            text-align: center;
            margin-bottom: 10px;
            
        }
        .contact-header h2 {
            color: #ff5722;
            font-weight: bold;
            letter-spacing: 2px;
            padding-bottom:0px;

        }
        .contact-header h1 {
            font-size: 48px;
            color: #0d1b2a;
            margin: 0;
            # padding-bottom:10px;
        }
        .contact-header span {
            color: #003366;
        }
        .submit-button {
            background-color: #003366;
            color: white;
            padding: 10px 30px;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            cursor: pointer;
        }
        .submit-button:hover {
            background-color: #0055aa;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Main container
    with st.container():
        st.markdown("<div class='contact-container'>", unsafe_allow_html=True)

        st.markdown("""
        <div class='contact-header'>
            <h2>CONNECT WITH US</h2>
            <h1>Let's Get In <span>Touch</span></h1>
        </div>
        """, unsafe_allow_html=True)

        with st.form(key='contact_form'):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Your Name (required)")
            with col2:
                phone = st.text_input("Your Phone (required)")

            col3, col4 = st.columns(2)
            with col3:
                email = st.text_input("Your Email (required)")
            with col4:
                topic = st.selectbox(
                    "Topic (required)",
    options=["", "Parking Issue", "App Feedback", "Technical Support", "Others"],  # Added an empty string as the first option
    index=0  # Set index to 0, so the first option (empty string) is selected by default
)

            message = st.text_area("Describe your issue here...", height=150)

            submit_button = st.form_submit_button(label='Send Message')

        st.markdown("</div>", unsafe_allow_html=True)

    # When form submitted
    if submit_button:
        if not name or not phone or not email or not topic or not message:
            st.error("Please fill in all required fields.")
            
        else:
            
            data=(name,phone,email,topic,message)
            login.mail(data)

        

elif st.session_state.current_page == "signup":
    st.markdown("""
    <style>
    /* Set background for the whole app container */
    .stApp {
        background-color: #f5f6ff; /* Light blue */
    }
    </style>
""", unsafe_allow_html=True)

# login
    if "page" not in st.session_state:
        st.session_state.page = "home"

    # Function to switch pages
    def go_to_login():
        st.session_state.page = "login"
        
    st.markdown("""
        <style>
        /* Container for signup */
        .signup-container {
            padding: 0.3rem;
            border-radius: 1rem;
            background-color: #FFFFFF; /* white */
            width: 100%;
            max-width: 400px;
            margin: auto;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }

        /* Style for input text boxes */
        .signup-container input {
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 10px;
            width: 100%;
            margin-bottom: 1rem;
            background-color: #FFFFFF;
        }

        /* Style for the Sign Up button */
        .signup-container button {
            background-color: black;
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.75rem;
            width: 100%;
            font-weight: bold;
            cursor: pointer;
        }

        /* Optional: Style the 'Already have an account?' */
        .signup-footer {
            text-align: center;
            margin-top: 0.5rem;
            font-size: 1rem;
            color: grey;
            padding-right:0px;
        }

        .signup-footer a {
            color: black;
            font-weight: bold;
            text-decoration: none;
        }
        </style>
    """, unsafe_allow_html=True)

# Now your form
    with st.container():
        st.markdown('<div class="signup-container"><h3 style="text-align:center;">Sign Up</h3>', unsafe_allow_html=True)

        name = st.text_input("Name")
        email = st.text_input("Email", placeholder="Your email would be your username!")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password:", type="password")
        if password != "" and confirm_password != "":
            if password == confirm_password:
                st.success("✅ Passwords match!")
            else:
                st.error("❌ Passwords do not match.")

        signup = st.button("Sign Up")
        if signup:
            if name == "" or password == "" or email == "":
                st.error("Please fill the form according to the instructions.")
            else:
                
                # st.subheader("Add More Details")
                # age = st.slider("Age", min_value=18, max_value=80)
                # contact = st.text_input("Contact")
                # address = st.text_input("Address")

                # if st.button("Submit More Details"):
                #     data=(age, contact, address, email)
                data = (name,email,password)
                login.reg(data)
                navigate_to("startsearch")
            

    col1, col2, col3, col4 = st.columns([1, 0.5, 0.5, 1])
    with col2:
        st.markdown("""
            <div class="signup-footer">
                Already have an account? 
            </div>
        """, unsafe_allow_html=True)
    with col3:
        already = st.button("Login", key="already",type="tertiary")
        if already:
            go_to_login()

    st.markdown('</div>', unsafe_allow_html=True)

    # Handle page navigation
    if st.session_state.page == "login":
        st.session_state.current_page ="login"




elif st.session_state.current_page == "login":

        st.markdown("""
                <style>
                /* Make the entire app background light blue */
                body, .stApp {
                    background-color:#f5f6ff!important;
                }

                /* Container for signup */
                .login-container {
                    padding: 0.3rem;
                    border-radius: 1rem;
                    background-color: #FFFFFF; /* white */
                    width: 100%;
                    max-width: 400px;
                    margin: auto;
                    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
                }

                </style>
            """, unsafe_allow_html=True)
        st.session_state.login_success = False
        st.markdown('<div class="login-container"><h3 style="text-align:center;">Login</h3>', unsafe_allow_html=True)
        contact = st.text_input("Username",placeholder="Your Email")
        password = st.text_input("Password", type="password")
        button= st.button("Login",key="login")
        if button:
            data = (contact,password)
            res=login.login(data)
            if res:
                st.success("Successfully Logged Into ParkEase!")
                st.session_state.login_success = True
            else:
                st.error("Invalid Credentials")
                st.session_state.login_success = False
            if st.session_state.get("login_success", False):
                navigate_to("startsearch")




elif st.session_state.current_page== "startsearch":
        st.markdown("""
        <style>
        /* Set background for the whole app container */
        .stApp {
            background-color: #f5f6ff; /* Light blue */
        }
        </style>
    """, unsafe_allow_html=True)
        col1, col2, col3 = st.columns([0.5, 1, 0.5])
        with col2:

        # choose you lot
            st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; padding-top: 50px;">
                <h1 style="
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    font-size: 36px;
                    bold: no;
                    color: #184676;
                    text-align: center;
                    margin: 0;
                ">
                    CHOOSE YOUR LOT
                </h1>
            </div>
        """, unsafe_allow_html=True)
        col1,col2,col3=st.columns(3)
        with col1:
                    st.image("space1pic.png")
                    level3_btn = st.button("Parking Lot 1")
                    if level3_btn:
                            space1w.space1()
        with col2:
                    st.image("space2pic.png")
                    level3_btn = st.button("Parking Lot 2")
                    if level3_btn:
                            space2w.space2()
        with col3:
            st.image("space3pic.png")
            level3_btn = st.button("Parking Lot 3")
            if level3_btn:
                        space3w.main()
                        

        
        home= st.button("Go Back to Home")
        if home:
            st.session_state.current_page = "home"
    
elif st.session_state.current_page =="profile":

    st.markdown("""
    <style>
    /* Set background for the whole app container */
    .stApp {
        background-color: #f5f6ff; /* Light blue */
    }
    </style>
""", unsafe_allow_html=True)

# --- Create Option Menu ---
    nav = option_menu(
                menu_title="",
                options=["Update Profile", "Delete Profile"],
                orientation="horizontal",
                styles={
                    "container": {
                        "padding": "0!important",
                        "background-color": "#f8f9fa",
                    },
                    "nav-link": {
                        "font-size": "18px",
                        "font-weight": "bold",
                        "text-align": "right",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {
                        "background-color": "#184676",
                        "color": "white",
                    }
                }
            )

            
    if nav=="Update Profile":
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False
        if "user_data" not in st.session_state:
            st.session_state.user_data = None

        # If user is not logged in
        if not st.session_state.logged_in:
            id = st.text_input("Username:")
            pw = st.text_input("Password:", type="password")
            yes = st.button("Submit")

            if yes:
                if id == "" or pw == "":
                    st.error("Incorrect Credentials")
                else:
                    data = (id, pw)
                    res = login.readone(data)

                    if res:
                        df = pd.DataFrame(res, columns=["name", "email", "password"])
                        st.session_state.logged_in = True
                        st.session_state.user_data = df
                    else:
                        st.error("User not found or wrong credentials")

        # If user is logged in, show the update form
        if st.session_state.logged_in and st.session_state.user_data is not None:
            df = st.session_state.user_data
            with st.form("update_user_info_form"):
                old_email = df["email"][0]
                old_password = df["password"][0]
                name = st.text_input('Name', value=df["name"][0])
                new_email = st.text_input("Email", value=df["email"][0])
                new_password = st.text_input('Password', type='password', value=df["password"][0])

                if st.form_submit_button("Update Info"):
                    if not all([old_email, old_password, name, new_email, new_password]):
                        st.warning("⚠️ Please fill in all fields.")
                    else:
                        success = login.update(name, new_email, new_password, old_email, old_password)
                        if success:
                            st.success("✅ User information updated successfully!")
                            # Update session state with new values
                            st.session_state.user_data = pd.DataFrame([[name, new_email, new_password]], columns=["name", "email", "password"])
                        else:
                            st.error("❌ Failed to update user information.")
        home= st.button("Go Back to Home")
        if home:
            st.session_state.current_page = "home"

    elif nav=="Delete Profile":
        id = st.text_input("Username:")
        pw = st.text_input("Password:", type="password")

        # Initial delete trigger
        if st.button("Delete"):
            if not id or not pw:
                st.error("❌ Please provide both username and password.")
            else:
                # Step 1: Check if user exists
                user = login.readone((id, pw))  # Make sure this returns None or [] if not found

                if user:
                    # Step 2: Store for confirmation
                    st.session_state.pending_delete = True
                    st.session_state.to_delete = (id, pw)
                else:
                    st.error("🚫 User not found or credentials incorrect.")

        # Step 3: If delete initiated, show confirmation
        if st.session_state.get("pending_delete", False):
            st.warning("⚠️ Are you sure you want to delete this user?")
            col1, col2 = st.columns(2)

            with col1:
                if st.button("Yes, Delete"):
                    try:
                        login.delete(st.session_state.to_delete)
                        st.success("✅ User deleted successfully!")
                        # Clear state
                        st.session_state.pending_delete = False
                        st.session_state.to_delete = None
                    except Exception as e:
                        st.error(f"❌ Error deleting user: {e}")

            with col2:
                if st.button("No, Cancel"):
                    st.info("❎ Deletion cancelled.")
                    st.session_state.pending_delete = False
                    st.session_state.to_delete = None
        home= st.button("Go Back to Home")
        if home:
            st.session_state.current_page = "home"





