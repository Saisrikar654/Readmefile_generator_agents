import streamlit as st
import requests

st.set_page_config(layout="wide")
main_url= "http://127.0.0.1:8000"
# def mainpage():
st.title("🤖 GitHub README Agent Squad")
st.subheader("Paste your messy notes, and watch our Tech Writer and Markdown Designer collaborate to build your portfolio documentation.")

col1, col2 = st.columns([1,2])
with col1:
    project_name = st.text_input("Enter your project name :--")
    project_desc = st.text_area("Enter about your project to create the Readme.md file with the data :--",height=350)
    btn=st.button("Generate README")
with col2:
    st.header("Output")
    preview_tab, code_tab = st.tabs(["Live Preview", "Raw Code"])
   
    
    if btn:
        if not project_name or not project_desc:
            st.error("Please fill the both project name and project details fileds")
        else: 
            with st.spinner("Agent 1 (tech writer) is analyzing the given info....."):
                try:
                    payload = {"project_name": project_name,"project_desc": project_desc}
                    res= requests.post(f"{main_url}/generate", json=payload)

                    if res.status_code == 200:
                        final_markdown = res.json().get("markdown", "")
                        #---------------------------------------
                        #.startswith is use to check the text is
                        #  matching or not if yes it return "true" else "false"
                        if final_markdown.startswith("```markdown"):
                            #.replace is use to the text with blank or user defined
                            #.rstrip is use to remove the backticks, newlines form the right side (r- right and strip-cut)
                            final_markdown = final_markdown.replace("```markdown", "", 1).rstrip("` \n")
                        elif final_markdown.startswith("```"):
                            final_markdown = final_markdown.replace("```", "", 1).rstrip("` \n")
                        #-------------------------------------------------------------------
                        st.success("Readme successfully optimized by the agent")

                        with preview_tab:
                            st.markdown(final_markdown)
                        with code_tab:
                            st.code(final_markdown, language="markdown")
                    else:
                        st.error("Backend error occured")
                except requests.exceptions.ConnectionError:
                    st.error("could not connected to fastapi")

    else:
        with preview_tab:
            st.info("Your visula README preview render here ")
        with code_tab:
            st.info("Your copy pasteable makedown code will appear here")