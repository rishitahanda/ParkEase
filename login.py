import streamlit as st
import sqlite3 
import re


def create_connection():
    conn=sqlite3.connect("parkease.db",check_same_thread=False)   
    return conn
conn=create_connection()
cursor=conn.cursor()

# 
def navigate_to(page):
    st.session_state.current_page = page
# 
def reg(data):
    name, email, password = data
    # validate email format
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com$"
    if not re.match(email_pattern, email):
        st.error("🚫 Invalid email format. Only .com emails are allowed.")
    # Then, block specific reserved usernames like "con"
    elif email.lower().endswith(".con"):
        st.error("🚫 'con' is not a valid email username.")
    else:
        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            st.error("🚫 This email is already registered. Please login instead.")
        else:
            try:
                # Insert new user
                cursor.execute('''INSERT INTO users(name, email, password) VALUES(?,?,?)''', (name, email, password))
                conn.commit()
                # from ParkEase import navigate_to
                # navigate_to("startsearch")
                navigate_to("startsearch")
            except Exception as e:
                st.error(f"An error occurred: {e}")
def login(data):
    try:
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", data)
        result = cursor.fetchone()
        if result:
            return result  # User found, credentials are correct
        else:
            st.warning("Invalid Credentials.")
            return None
    except Exception as e:
        st.error(f"Something went wrong: {e}")
        return None

def update(name, new_email, new_password, old_email, old_password):
    try:
        if new_email != old_email:
            cursor.execute(
                "SELECT * FROM users WHERE email = ?",
                (new_email,)
            )
            if cursor.fetchone():
                st.error("🚫 The new email is already registered with another account.")
                return False

        # Step 3: Proceed with update
        cursor.execute(
            "UPDATE users SET name = ?, email = ?, password = ? WHERE email = ? AND password = ?",
            (name, new_email, new_password, old_email, old_password)
        )
        conn.commit()

        if cursor.rowcount == 0:
            st.warning("⚠️ No changes were made.")
            return False

        return True

    except Exception as e:
        st.error(f"Something went wrong: {e}")
        return False



def readone(data):
    try:
        old_email = data[0].strip()
        old_password = data[1].strip()

        cursor.execute(
            "SELECT * FROM users WHERE email = ? AND password = ?",
            (old_email, old_password)
        )
        user = cursor.fetchone()

        if not user:
            st.error("❌ Incorrect Credentials")
            return None  # Return None instead of False
        else:
            return [user]  # Return as a list of one tuple, so DataFrame works
    except Exception as e:
        st.error(f"Something went wrong: {e}")
        return None

def delete(data):
    try:
        cursor.execute("DELETE FROM users WHERE email = ? AND password = ?", data)
        if cursor.rowcount==0:
            return False
        else:
            conn.commit()
            return True
    except sqlite3.Error as e:
            st.error(f"SQLite Error: {str(e)}")
            print(f"SQLite Error: {str(e)}")


def mail(data):
    name, phone, email, topic, message = data

    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com$"
    phone_pattern = r"^\d{10}$"  # Exactly 10 digits

    # Validate email format
    if not re.match(email_pattern, email):
        st.error("🚫 Invalid email format. Only .com emails are allowed.")

    # Disallow .con emails
    elif email.lower().endswith(".con"):
        st.error("🚫 '.con' is not a valid email domain.")

    # Validate phone number
    elif not re.match(phone_pattern, phone):
        st.error("🚫 Phone number must be exactly 10 digits (numbers only).")

    else:
        try:
            cursor.execute(
                '''INSERT INTO email(name, phone, email, topic, message)
                   VALUES (?, ?, ?, ?, ?)''',
                data
            )
            conn.commit()
            st.success("✅ Message sent successfully!")
        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")

