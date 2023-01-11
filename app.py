import pandas as pd
import numpy as np
import streamlit as st
import pickle
from PIL import Image
model = pickle.load(open("job_post.pkl","rb"))

def prediction(pred):
   if pred == 0:
      return ("The Job Is Real")
   else:
      return ("The Job Is Fake")
html_temp = """
    <div style='background-color: teal; padding:10px'>
    <h2 style='color:white; text-align:center;'>Real And Fake Job Posting Detection</h2>
    </div>"""

st.markdown(html_temp, unsafe_allow_html=True)
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)

st.image("""https://imagevars.gulfnews.com/2020/09/07/Fake-job-offer_1746917114d_original-ratio.jpg""")
def main():
   st.header('Enter the details:')
   telecommuting=st.radio("Does Working From Home Allowed?", options=["Yes","No"])
   if telecommuting=="No":
       telecommuting=0
   else:
       telecommuting=1
   has_company_logo=st.radio("Does The Company Got Any Logo? ",options=["Yes","No"])
   if has_company_logo=="No":
        has_company_logo=0
   else:
        has_company_logo=1
   has_questions=st.radio("Does The Recruiter Asked Any Questions",options=["Yes","No"])
   if has_questions=="No":
       has_questions=0
   else:
       has_questions=1
   employment_type=st.selectbox("What Type Of Employement",
                             options=["Select","Other","Full-time","Employement_Unavailable","Part-time",
                              "Contract","Temporary"])
   if employment_type=="Other":
        employment_type=0
   elif employment_type=="Full-time":
        employment_type=1
   elif employment_type=="Employement_Unavailable":
        employment_type=2
   elif employment_type=="Part-time":
        employment_type=3
   elif employment_type=="Contract":
        employment_type=4
   elif employment_type=="Temporary":
        employment_type=5
   required_experience=st.selectbox("What Type Of Experience Required",options=["Select","Internship","Not Applicable",
                                 "Experience_Unavailable","Mid-Senior level","Associate","Entry level","Executive",
                                                                     "Director"])
   if required_experience=="Internship":
        required_experience=0
   elif required_experience=="Not Applicable":
        required_experience=1
   elif required_experience=="Experience_Unavailable":
        required_experience=2
   elif required_experience=="Mid-Senior level":
        required_experience=3
   elif required_experience=="Associate":
        required_experience=4
   elif required_experience=="Entry level":
        required_experience=5
   elif required_experience=="Executive":
        required_experience=6
   elif required_experience=="Director":
        required_experience=7
   required_education=st.selectbox("What\'s The Highest Educcatin Required",options=["Select","Education_Unavailable",
                                "Bachelor's Degree","Master's Degree","High School or equivalent",
                                "Unspecified","Some College Coursework Completed","Vocational",
                                "Certification","Associate Degree","Professional","Doctorate",
                                "Some High School Coursework","Vocational - Degree","Vocational - HS Diploma"])
   if required_education=="Education_Unavailable":
      required_education=0
   elif required_education=="Bachelor's Degree":
      required_education=1
   elif required_education=="Master's Degree":
      required_education=2
   elif required_education=="High School or equivalent":
      required_education=3
   elif required_education=="Unspecified":
      required_education=4
   elif required_education=="Some College Coursework Completed":
      required_education=5
   elif required_education=="Vocational":
      required_education=6
   elif required_education=="Certification":
      required_education=7
   elif required_education=="Associate Degree":
      required_education=8
   elif required_education=="Professional":
      required_education=9
   elif required_education=="Doctorate":
      required_education=10
   elif required_education=="Some High School Coursework":
      required_education=11
   elif required_education=="Vocational - Degree":
      required_education=12
   elif required_education=="Vocational - HS Diploma":
      required_education=13
   industry=st.selectbox("What Typpe Of Industry",options=["Select","Not_Specified","Marketing and Advertising","Computer Software",
                                                "Hospital & Health Care","Online Media","Information Technology and Services","Financial Services","Management Consulting",
                                                "Events Services","Internet","Facilities Services","Consumer Electronics","Telecommunications","Consumer Services","Construction",
                                                "Oil & Energy","Education Management","Building Materials","Banking","Food & Beverages","Food Production",
                                                "Health, Wellness and Fitness","Insurance","E-Learning","Cosmetics","Staffing and Recruiting",
                                                "Venture Capital & Private Equity","Leisure, Travel & Tourism","Human Resources","Pharmaceuticals","Farming","Legal Services",
                                                "Luxury Goods & Jewelry","Machinery","Real Estate","Mechanical or Industrial Engineering","Public Relations and Communications",
                                                "Consumer Goods","Medical Practice","Electrical/Electronic Manufacturing","Hospitality","Music","Market Research","Automotive",
                                                "Philanthropy","Utilities","Primary/Secondary Education","Logistics and Supply Chain","Design","Gambling & Casinos","Accounting",
                                                "Environmental Services","Mental Health Care","Investment Management","Apparel & Fashion","Media Production",
                                                "Publishing","Medical Devices","Information Services","Retail","Sports","Computer Games","Chemicals","Aviation & Aerospace",
                                                "Business Supplies and Equipment","Program Development","Computer Networking","Biotechnology","Civic & Social Organization","Religious Institutions",
                                                "Warehousing","Airlines/Aviation","Writing and Editing","Restaurants","Outsourcing/Offshoring","Transportation/Trucking/Railroad",
                                                "Wireless","Investment Banking","Nonprofit Organization Management","Libraries","Computer Hardware","Broadcast Media","Printing",
                                                "Graphic Design","Entertainment","Wholesale","Research","Animation","Government Administration","Capital Markets",
                                                "Computer & Network Security","Semiconductors","Security and Investigations","Architecture & Planning",
                                                "Maritime","Fund-Raising","Higher Education","Renewables & Environment","Motion Pictures and Film",
                                                "Law Practice","Government Relations","Packaging and Containers","Sporting Goods","Mining & Metals","Import and Export",
                                                "International Trade and Development","Professional Training & Coaching","Textiles","Commercial Real Estate","Law Enforcement",
                                                "Package/Freight Delivery","Translation and Localization","Photography","Industrial Automation","Wine and Spirits","Public Safety","Civil Engineering","Military",
                                                "Defense & Space","Veterinary","Executive Office","Performing Arts","Individual & Family Services","Public Policy",
                                                "Nanotechnology","Museums and Institutions","Fishery","Plastics","Furniture","Shipbuilding","Alternative Dispute Resolution","Ranching"])
   if industry=="Not_Specified":
    industry=0
   elif industry=="Marketing and Advertising":
      industry=1
   elif industry=="Computer Software":
    industry=2
   elif industry=="Hospital & Health Care":
    industry=3
   elif industry=="Online Media":
     industry=4
   elif industry=="Information Technology and Services":
    industry=5
   elif industry=="Financial Services":
    industry=6
   elif industry=="Management Consulting":
    industry=7
   elif industry=="Events Services":
    industry=8
   elif industry=="Internet":
    industry=9
   elif industry=="Facilities Services":
    industry=10
   elif industry=="Consumer Electronics":
    industry=11
   elif industry=="Telecommunications":
    industry=12
   elif industry=="Consumer Services":
    industry=13
   elif industry=="Construction":
    industry=14
   elif industry=="Oil & Energy":
    industry=15
   elif industry=="Education Management":
     industry=16
   elif industry=="Building Materials":
    industry=17
   elif industry=="Banking":
     industry=18
   elif industry=="Food & Beverages":
     industry=19
   elif industry=="Food Production":
     industry=20
   elif industry=="Health, Wellness and Fitness":
     industry=21
   elif industry=="Insurance":
     industry=22
   elif industry=="E-Learning":
     industry=23
   elif industry=="Cosmetics":
     industry=24
   elif industry=="Staffing and Recruiting":
     industry=25
   elif industry=="Venture Capital & Private Equity":
     industry=26
   elif industry=="Leisure, Travel & Tourism":
     industry=27
   elif industry=="Human Resources":
     industry=28
   elif industry=="Pharmaceuticals":
     industry=29
   elif industry=="Farming":
     industry=30
   elif industry=="Legal Services":
     industry=31
   elif industry=="Luxury Goods & Jyewelry":
     industry=32
   elif industry=="Machinery":
     industry=33
   elif industry=="Real Estate":
     industry=34
   elif industry=="Mechanical or Industrial Engineering":
     industry=35
   elif industry=="Public Relations and Communications":
     industry=36
   elif industry=="Consumer Goods":
     industry=37
   elif industry=="Medical Practice":
     industry=38
   elif industry=="Electrical/Electronic Manufacturing":
     industry=39
   elif industry=="Hospitality":
     industry=40
   elif industry=="Music":
     industry=41
   elif industry=="Market Research":
     industry=42
   elif industry=="Automotive":
     industry=43
   elif industry=="Philanthropy":
     industry=44
   elif industry=="Utilities":
     industry=45
   elif industry=="Primary/Secondary Education":
     industry=46
   elif industry=="Logistics and Supply Chain":
     industry=47
   elif industry=="Design":
     industry=48
   elif industry=="Gambling & Casinos":
     industry=49
   elif industry=="Accounting":
     industry=50
   elif industry=="Environmental Services":
     industry=51
   elif industry=="Mental Health Care":
     industry=52
   elif industry=="Investment Management":
     industry=53
   elif industry=="Apparel & Fashion":
     industry=54
   elif industry=="Media Production":
     industry=55
   elif industry=="Publishing":
     industry=56
   elif industry=="Medical Devices":
     industry=57
   elif industry=="Information Services":
     industry=58
   elif industry=="Retail":
     industry=59
   elif industry=="Sports":
     industry=60
   elif industry=="Computer Games":
     industry=61
   elif industry=="Chemicals":
     industry=62
   elif industry=="Aviation & Aerospace":
     industry=63
   elif industry=="Business Supplies and Equipment":
     industry=64
   elif industry=="Program Development":
     industry=65
   elif industry=="Computer Networking":
     industry=66
   elif industry=="Biotechnology":
     industry=67
   elif industry=="Civic & Social Organization":
     industry=68
   elif industry=="Religious Institutions":
     industry=69
   elif industry=="Warehousing":
     industry=70
   elif industry=="Airlines/Aviation":
     industry=71
   elif industry=="Writing and Editing":
     industry=72
   elif industry=="Restaurants":
      industry=73
   elif industry=="Outsourcing/Offshoring":
     industry=74
   elif industry=="Transportation/Trucking/Railroad":
     industry=75
   elif industry=="Wireless":
     industry=76
   elif industry=="Investment Banking":
     industry=77
   elif industry=="Nonprofit Organization Management":
     industry=78
   elif industry=="Libraries":
     industry=79
   elif industry=="Computer Hardware":
     industry=80
   elif industry=="Broadcast Media":
     industry=81
   elif industry=="Printing":
     industry=82
   elif industry=="Graphic Design":
     industry=83
   elif industry=="Entertainment":
     industry=84
   elif industry=="Wholesale":
     industry=85
   elif industry=="Research":
     industry=86
   elif industry=="Animation":
     industry=87
   elif industry=="Government Administration":
     industry=88
   elif industry=="Capital Markets":
     industry=89
   elif industry=="Computer & Network Security":
     industry=90
   elif industry=="Semiconductors":
     industry=91
   elif industry=="Security and Investigations":
     industry=92
   elif industry=="Architecture & Planning":
     industry=93
   elif industry=="Maritime":
     industry=94
   elif industry=="Fund-Raising":
     industry=95
   elif industry=="Higher Education":
     industry=96
   elif industry=="Renewables & Environment":
     industry=97
   elif industry=="Motion Pictures and Film":
     industry=98
   elif industry=="Law Practice":
     industry=99
   elif industry=="Government Relations":
     industry=100
   elif industry=="Packaging and Containers":
     industry=101
   elif industry=="Sporting Goods":
     industry=102
   elif industry=="Mining & Metals":
     industry=103
   elif industry=="Import and Export":
      industry=104
   elif industry=="International Trade and Development":
     industry=105
   elif industry=="Professional Training & Coaching":
     industry=106
   elif industry=="Textiles":
     industry=107
   elif industry=="Commercial Real Estate":
     industry=108
   elif industry=="Law Enforcement":
     industry=109
   elif industry=="Package/Freight Delivery":
     industry=110
   elif industry=="Translation and Localization":
     industry=111
   elif industry=="Photography":
     industry=112
   elif industry=="Industrial Automation":
     industry=113
   elif industry=="Wine and Spirits":
     industry=114
   elif industry=="Public Safety":
     industry=115
   elif industry=="Civil Engineering":
     industry=116
   elif industry=="Military":
     industry=117
   elif industry=="Defense & Space":
     industry=118
   elif industry=="Veterinary":
     industry=119
   elif industry=="Executive Office":
     industry=120
   elif industry=="Performing Arts":
     industry=121
   elif industry=="Individual & Family Services":
     industry=122
   elif industry=="Public Policy":
     industry=123
   elif industry=="Nanotechnology":
     industry=124
   elif industry=="Museums and Institutions":
     industry=125
   elif industry=="Fishery":
     industry=126
   elif industry=="Plastics":
     industry=127
   elif industry=="Furniture":
     industry=128
   elif industry=="Shipbuilding":
     industry=129
   elif industry=="Alternative Dispute Resolution":
     industry=130
   elif industry=="Ranching":
     industry=131
   function=st.selectbox("What Type Of Function Mentioned",options=["Select","Marketing","Customer Service","Not_Specified",
                      "Sales","Health Care Provider","Management","Information Technology","Other",
                      "Engineering","Administrative","Design","Production","Education","Supply Chain",
                      "Business Development","Product Management","Financial Analyst","Consulting","Human Resources",
                      "Project Management","Manufacturing","Public Relations","Strategy/Planning","Advertising",
                      "Finance","General Business","Research","Accounting/Auditing","Art/Creative","Quality Assurance",
                      "Data Analyst","Business Analyst","Writing/Editing","Distribution","Science","Training",
                      "Purchasing","Legal"])
   if function=="Marketing":
    function=0
   elif function=="Customer Service":
    function=1
   elif function=="Not_Specified":
    function=2
   elif function=="Sales":
    function=3
   elif function=="Health Care Provider":
    function=4
   elif function=="Management":
    function=5
   elif function=="Information Technology":
    function=6
   elif function=="Other":
    function=7
   elif function=="Engineering":
    function=8
   elif function=="Administrative":
    function=9
   elif function=="Design":
    function=10
   elif function=="Production":
    function=11
   elif function=="Education":
    function=12
   elif function=="Supply Chain":
    function=13
   elif function=="Business Development":
    function=14
   elif function=="Product Management":
    function=15
   elif function=="Financial Analyst":
    function=16
   elif function=="Consulting":
    function=17
   elif function=="Human Resources":
    function=18
   elif function=="Project Management":
    function=19
   elif function=="Manufacturing":
    function=20
   elif function=="Public Relations":
    function=21
   elif function=="Strategy/Planning":
    function=22
   elif function=="Advertising":
    function=23
   elif function=="Finance":
    function=24
   elif function=="General Business":
    function=25
   elif function=="Research":
    function=26
   elif function=="Accounting/Auditing":
    function=27
   elif function=="Art/Creative":
    function=28
   elif function=="Quality Assurance":
    function=29
   elif function=="Data Analyst":
    function=30
   elif function=="Business Analyst":
    function=31
   elif function=="Writing/Editing":
    function=32
   elif function=="Distribution":
    function=33
   elif function=="Science":
    function=34
   elif function=="Training":
    function=35
   elif function=="Purchasing":
    function=36
   elif function=="Legal":
    function=37

   result=[[telecommuting,has_company_logo,has_questions,employment_type,required_experience,required_education,industry,function]]
   if st.button('Check The Prediction'):
      st.success(prediction(model.predict(result)))

if __name__== "__main__":
    main()

