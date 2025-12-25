# --------- Streamlit Core Library ---------
import streamlit as st  
# Streamlit is used to build interactive web apps in Python

# --------- Streamlit Page Configuration ---------
st.set_page_config(page_title="Parkease",page_icon=":parking:",layout="wide")

# --------- Streamlit Option Menu ---------
from streamlit_option_menu import option_menu  
# Used to create styled horizontal/vertical option menus

# --------- Data Manipulation ---------
import pandas as pd  
# Used for handling tabular data, not actively used in this code but imported

# --------- Streamlit Lottie (Animation Renderer) ---------
from streamlit_lottie import st_lottie  
# Used to render Lottie JSON animations (GIF-like visuals) in Streamlit apps

# --------- Base64 (Built-in Python Module) ---------
import base64  
# Used to encode image and video files in base64 for embedding into HTML/CSS

# --------- Custom Modules (Your Own Python Scripts) ---------
import login
# Handles sql database functions
import space1
# Contains functions related to Parking Lot of Ambience Mall
import space2
# Contains functions related to Parking Lot of Fun City
import space3
# Contains functions related to Parking Lot of City Center




# Convert local image to base64 for embedding inside the box
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Function to convert image to base64 so it can be embedded in file (used for logo)
image_path = "parkeasename.jpg"  # Ensure this file exists in the same directory
image_base64 = get_base64_image(image_path)

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# session's state function for each button
def navigate_to(page):
    st.session_state.current_page = page

# Inject CSS for the blurred GIF background and box
st.markdown("""
    <hr style="border: none; height: 4px; background-color: #455262; margin: 20px 0;">
""", unsafe_allow_html=True)

# Navigation Buttons
col1, col2, col3, col4, col5, col6 = st.columns([1,2,1,1,1,1])
with col1:
    st.image(image_path)
# with col2: empty space
with col3:
    if st.button("Home",type="tertiary"):
        navigate_to("home")
        st.rerun()
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
        

    lottie_url = "https://lottie.host/60f7abba-e34f-406c-a757-07e91752c22b/t2TNsUCczo.json"  # Replace if needed
    st.markdown("""
        <style>
        
        .full-width-lottie > div {
            display: flex;
            justify-content: center;
            align-items: center;
            padding-bottom : 0px;
        }
        .full-width-lottie canvas {
            width: 100% !important;
            height: 1% !important;
            padding-bottom : 0px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Display Lottie inside a styled container
    with st.container():
        with st.container():
            st.markdown('<div class="full-width-lottie">', unsafe_allow_html=True)
            st_lottie(
                lottie_url,
                speed=1,
                loop=True,
                quality="low",
                key="lottie-banner"
            )
            st.markdown('</div>', unsafe_allow_html=True)
# CONTACT US
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f6ff;
            margin-top: 0%;
        }
        .contact-container {
            width: 100%;
            min-height: 10vh;
            background-color: #f5f6ff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 0%;
            
        }
        .contact-header {
            text-align: center;
            margin-bottom: 10px;
            margin-top: 0%;
            
        }
        .contact-header h2 {
            color: #ff5722;
            font-weight: bold;
            letter-spacing: 2px;
            padding-bottom:0px;
            padding-top : 0px;

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
    options=["", "Parking Issue", "App Feedback", "Technical Support", "Others"],  
    # Added an empty string as the first option
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
    col1, col2, col3 = st.columns([0.5, 1, 0.5])
    with col2:
        if st.button("Let's Park",key="lets park",use_container_width=True):
            park_action()
        

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
    with open("signin.gif", "rb") as f:
        gif_bytes = f.read()
    encoded_gif = base64.b64encode(gif_bytes).decode()
    with open("thankyou.gif", "rb") as f:
        thankyou_gif = base64.b64encode(f.read()).decode()

    # Styling
    st.markdown("""
        <style>
        
        .signup-container {
            padding: 0rem;
            border-radius: 1rem;
            background-color: #FFFFFF;
            width: 100%;
            max-width: 400px;
            margin: 0 auto;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .signup-heading-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
        }
        .signup-heading-container h3 {
            margin: 0;
            padding: 5px;
        }
        .signup-gif img {
            width: 100px;
            height: 100px;
            border-radius: 8px;
        }
        .signup-footer {
            text-align: center;
            margin-top: 0.5rem;
            font-size: 1rem;
            color: grey;
        }
        </style>
    """, unsafe_allow_html=True)

    # Signup Form with Form API
    with st.container():
        st.markdown(f"""
            <div class="signup-container">
                <div class="signup-heading-container">
                    <h3>Sign Up</h3>
                    <div class="signup-gif">
                        <img src="data:image/gif;base64,{encoded_gif}" alt="signup animation">
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        with st.form(key="signup_form"):
            full_name = st.text_input("Name", placeholder="Enter your name")
            email = st.text_input("Email", placeholder="Enter your email, This will be your UserName!")
            password = st.text_input("Password", type="password", placeholder="Create a password")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")

            signup_clicked = st.form_submit_button("Sign Up")

        if signup_clicked:
            if password == confirm_password and full_name and email:
                data=(full_name,email,password)
                login.reg(data)
                
            else:
                st.error("Please ensure all fields are filled and passwords match.")
            
        col1, col2, col3, col4 = st.columns([1, 0.5, 0.5, 1])
        with col2:
                st.markdown("""
                    <div class="signup-footer">
                        Already have an account? 
                    </div>
                """, unsafe_allow_html=True)
        with col3:
                already = st.button("Login",key="login",type="tertiary")
                if already:
                    go_to_login()
        # with col4:
        #     home= st.button("Home", key="home", type="tertiary")
        #     if home:
        #         navigate_to("home")

    st.markdown('</div>', unsafe_allow_html=True)

    # Handle page navigation
    if st.session_state.page == "login":
        st.session_state.current_page ="login"



elif st.session_state.current_page == "login":
        def get_gif_base64(file_path):
            with open(file_path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode("utf-8")

        gif_base64 = get_gif_base64("login.gif")
        st.markdown("""
        <style>
        body, .stApp {
            background-color:#f5f6ff!important;
        }
        .login-container {
            padding: 0rem;
            border-radius: 1rem;
            background-color: #FFFFFF;
            width: 100%;
            max-width: 400px;
            margin: auto;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .login-header {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 0rem;
        }
        .login-header img {
            width: 48px;
            height: 0px;
        }
        </style>
            """, unsafe_allow_html=True)

        # If already logged in, show logout button instead
        if st.session_state.get("login_success", False):
            navigate_to("startsearch")
        
        else:        
            st.session_state.login_success = False
            st.markdown(f"""
                    <div class="login-container">
                        <div class="login-header">
                            <h3>Login</h3>
                            <img src="data:image/gif;base64,{gif_base64}" alt="gif" style="width: 100px; height: 100px;">
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            email = st.text_input("Username", placeholder="Your Email is your Username.")
            password = st.text_input("Password", type="password")
            button = st.button("Login", key="login")

            if button:
                    data = (email, password)
                    res = login.login(data)
                    if res:
                        st.success("Successfully Logged Into ParkEase!")
                        st.session_state.login_success = True
                        navigate_to("startsearch")
                    else:
                        st.session_state.login_success = False

if st.session_state.current_page == "startsearch":
        st.session_state.login_success = True

        def space1_func():
            space1.space1()

        def space2_func():
            space2.space2()

        def space3_func():
            space3.main()

        if st.session_state.login_success ==  True:
            navigate_to("startsearch")

        # Redirect to login if not authenticated
        # if not st.session_state.get("login_success", False):
        #     navigate_to("login")

        # Style
        st.markdown("""
            <style>
            .stApp {
                background-color: #f5f6ff;
            }
            .custom-heading {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-size: 36px;
                color: #184676;
                text-align: center;
                margin-top: 0px;
                
            }
            .selectbox-label {
                text-align: center;
            }
            .logout-button {
                position: absolute;
                top: 10px;
                right: 20px;
            }
            </style>
        """, unsafe_allow_html=True)

        # Logout button in top-right corner
        col_a, col_b = st.columns([9, 1])
        with col_b:
            if st.button("Logout", key="out"):
                st.session_state.login_success = False
                navigate_to("home")

        # Centered heading
        col1, col2, col3 = st.columns([0.5, 5, 0.5])
        with col2:
            st.markdown('<div class="custom-heading">WELCOME TO PARKEASE</div>',unsafe_allow_html=True)
            st.markdown('<div class="custom-heading">CHOOSE YOUR DESTINATION</div>', unsafe_allow_html=True)
            destination = st.selectbox(" ", ["Select a place", "Ambience Mall", 
                                            "Fun City", "City Center"])

        # Parking lot mapping
        place_to_lot = {
            "Ambience Mall": {"img": "mall.jpg", "label": "Open Parking Lot", "func": space1_func},
            "Fun City": {"img": "ccc.png", "label": "Open Parking Lot", "func": space2_func},
            "City Center": {"img": "center.png", "label": "Open Parking Lot", "func": space3_func},
        }

        # Show lot info based on destination
        if destination != "Select a place":
            lot = place_to_lot[destination]

            col_left, col_main, col_right = st.columns([1, 3, 1])
            with col_main:
                st.image(lot["img"], use_container_width=True)
                if st.button(lot["label"]):
                    lot["func"]()
    
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





