###############################
# This program lets you       #
# - enter values in Streamlit #
# - get prediction            #  
###############################
import pickle
#from turtle import st

import pandas as pd
import streamlit as st

# loading the model
 #path = ''
modelname = 'toymodel_02.pkl'
loaded_model = pickle.load(open(modelname, 'rb'))

#############
# Main page #
#############                
st.write("The model prediction")

# LIVINGAPARTMENTS_AVG_MIN = 0.0
# LIVINGAPARTMENTS_AVG_MAX = 1.0
# APARTMENTS_AVG_MIN = 0.0
# APARTMENTS_AVG_MAX = 0.11697126743049956

# Get input values - numeric variables
# LIVINGAPARTMENTS_AVG = st.slider('Please enter the living apartments:',
#                                 min_value=LIVINGAPARTMENTS_AVG_MIN,
#                                 max_value=LIVINGAPARTMENTS_AVG_MAX
#                                 )
# APARTMENTS_AVG = st.slider('Please enter the apartment average:',
#                           min_value=APARTMENTS_AVG_MIN,
#                         max_value=APARTMENTS_AVG_MAX
#                           )

# Set dummy variables to zero    
cat_list = ['nom_q_9103b', 'nom_q_9103c', 'nom_q_9103d', 'nom_q_9103e',
            'nom_q_9103f', 'nom_q_9103g', 'nom_q_9103h', 'nom_q_9103i',
            'nom_q_9103j', 'nom_q_9103k', 'nom_q_9103l', 'nom_q_9103m',
            'nom_q_9103n', 'nom_q_9103o', 'nom_q_9103p', 'nom_q_9103q',
            'nom_q_9103r', 'nom_q_9103s', 'nom_q_9204']
for i in cat_list:
    exec("%s = %d" % (i, 0))  # The exec() command makes a value as the variable name

# Enter data for prediction
nom_q_9103b = st.selectbox('(nom_q_9103_b)',
                           ('Electronics',
                            'Chemistry')
                           )
nom_q_9103c = st.selectbox('(nom_q_9103_c)',
                           ('Photography',
                            'Botany')
                           )
nom_q_9103d = st.selectbox('(nom_q_9103d)',
                           ('Owning a store',
                            'Advice on work')
                           )
nom_q_9103e = st.selectbox('(nom_q_9103e)',
                           ('Company management',
                            'Helping families in need')
                           )
nom_q_9103f = st.selectbox('(nom_q_9103f)',
                           ('Physical training',
                            'Doktor')
                           )
nom_q_9103g = st.selectbox('(nom_q_9103g)',
                           ('Music',
                            'Working with wood')
                           )
nom_q_9103h = st.selectbox('(nom_q_9103h)',
                           ('Physics',
                            'Economic sciences')
                           )
nom_q_9103i = st.selectbox('(nom_q_9103i)',
                           ('Education',
                            'Art')
                           )
nom_q_9103j = st.selectbox('(nom_q_9103j)',
                           ('Law',
                            'Artist / Folk Crafts')
                           )
nom_q_9103k = st.selectbox('(nom_q_9103k)',
                           ('Child care',
                            'Stand electronics')
                           )

nom_q_9103l = st.selectbox('(nom_q_9103l)',
                           ('Landscaping',
                            'Playing in a group, being a member of a music team')
                           )
nom_q_9103m = st.selectbox('(nom_q_9103m)',
                           ('Travel agent',
                            'Mechanic')
                           )
nom_q_9103n = st.selectbox('(nom_q_9103n)',
                           ('Work in the office',
                            'Picture description')
                           )
nom_q_9103o = st.selectbox('(nom_q_9103o)',
                           ('Forest',
                            'The nurse of mercy')
                           )
nom_q_9103p = st.selectbox('(nom_q_9103p)',
                           ('Electric', 'Economist'))

nom_q_9103q = st.selectbox('(nom_q_9103q)',
                           ('Accounting', 'Geology'))

nom_q_9103r = st.selectbox('(nom_q_9103r)',
                           ('Builder', 'Economist'))

nom_q_9103s = st.selectbox('(nom_q_9103s)',
                           ('Confirmation of a home loan (mortgage)',
                            'Helping patients in the hospital')
                           )



if nom_q_9103b == 'Electronics':
    Electronics = 1
elif nom_q_9103b == 'Chemistry':
    Chemistry = 1

elif nom_q_9103c == 'Botany':
    Botany = 1
elif nom_q_9103c == 'Photography':
    Photography = 1

elif nom_q_9103d == 'Owning_store':
    Owning_store = 1
elif nom_q_9103d == 'Advice_on_work':
    Advice_on_work = 1

elif nom_q_9103e == 'Company_management':
    Company_management = 1
elif nom_q_9103e == 'Helping_families_in_need':
    Helping_families_in_need = 1

elif nom_q_9103f == 'Physical_training':
    Physical_training = 1
elif nom_q_9103f == 'Doktor':
    Doktor = 1

elif nom_q_9103g == 'Music':
    Music = 1
elif nom_q_9103g == 'Working_with_wood':
    Working_with_wood = 1

elif nom_q_9103h == 'Physics':
    Physics = 1
elif nom_q_9103h == 'Economic_sciences':
    Economic_sciences = 1

elif nom_q_9103i == 'Education':
    Education = 1
elif nom_q_9103i == 'Art':
    Art = 1

if nom_q_9103j == 'Law':
    Law = 1
elif nom_q_9103j == 'Artist_Folk_Crafts':
    Artist_Folk_Crafts = 1

elif nom_q_9103k == 'Child_care':
    Child_care = 1
elif nom_q_9103k == 'Stand_electronics':
    Stand_electronics = 1


elif nom_q_9103l == 'Landscaping':
    Landscaping = 1
elif nom_q_9103l == 'Playing_in_group':
    Playing_in_group = 1

elif nom_q_9103m == 'Travel_agent':
    Travel_agent = 1
elif nom_q_9103m == 'Mechanic':
    Mechanic = 1

elif nom_q_9103n == 'Work_office':
    Work_office = 1
elif nom_q_9103n == 'Picture_description':
    Picture_description = 1

elif nom_q_9103o == 'nurse_mercy':
    nurse_mercy = 1
elif nom_q_9103o == 'Forest':
    Forest = 1

elif nom_q_9103p == 'Economist':
    Economist = 1
elif nom_q_9103p == 'Electric':
    Electric = 1

elif nom_q_9103q == 'Accounting':
    Accounting = 1
elif nom_q_9103q == 'Geology':
    Geology = 1

elif nom_q_9103r == 'Economist':
    Economist = 1
elif nom_q_9103r == 'Builder':
    Builder = 1

elif nom_q_9103s == 'helping_hospital':
    helping_hospital = 1
elif nom_q_9103s == 'mortgage':
    mortgage = 1

#elif nom_q_9204 == 'OTHER':
 #   OTHER = 1
# when 'Predict' is clicked, make the prediction and store it 
if st.button("Get Your Prediction"):
    X = pd.DataFrame({'nom_q_9103b': [nom_q_9103b],
                          'nom_q_9103c': [nom_q_9103c],
                          'nom_q_9103d': [nom_q_9103d],
                          'nom_q_9103e': [nom_q_9103e],
                          'nom_q_9103f': [nom_q_9103f],
                          'nom_q_9103g': [nom_q_9103g],
                          'nom_q_9103h': [nom_q_9103h],
                          'nom_q_9103i': [nom_q_9103i],
                          'nom_q_9103j': [nom_q_9103j],
                          'nom_q_9103k': [nom_q_9103k],
                          'nom_q_9103l': [nom_q_9103l],
                          'nom_q_9103m': [nom_q_9103m],
                          'nom_q_9103n': [nom_q_9103n],
                          'nom_q_9103o': [nom_q_9103o],
                          'nom_q_9103p': [nom_q_9103p],
                          'nom_q_9103q': [nom_q_9103q],
                          'nom_q_9103r': [nom_q_9103r],
                          'nom_q_9103s': [nom_q_9103s],
                          })
    # Making predictions            
    #prediction = loaded_model.predict(X)[:, 1]  # The model produces (p0,p1), we want p1.
    predictions = loaded_model.predict(X)

    st.success('Your Target is {}'.format(predictions))
