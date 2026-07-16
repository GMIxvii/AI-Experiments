import streamlit as st
from experta import *
from streamlit_extras.stateful_button import button
from streamlit_extras.bottom_container import bottom


class Symptom(Fact):
    nom = Field(str)

class Diagnosis(Fact):
    maladie = Field(str)

class Medication(Fact):
    name = Field(str)
    dosage = Field(str)
    note = Field(str)

class PatientInformation(Fact):
    age = Field(int)
    weight = Field(int)
    health_questions = Field(dict)


medications = {
    "Strep throat bacterial infection": [
        Medication(name="Amoxicillin", dosage="Adult: 500mg every 8 hours, Child: 20mg/kg every 8 hours", note="Take for 10 days"),
        Medication(name="Cephalexin", dosage="Adult: 500mg every 6 hours, Child: 25mg/kg every 6 hours", note="Take for 10 days"),
        Medication(name="Oral Penicillin V", dosage="Adult: 500mg every 6 hours, Child: 250mg twice daily or 250mg three times daily", note="Take for 10 days"),
        Medication(name="Oral Amoxicillin", dosage="Adult: 500mg every 8 hours, Child: 50mg/kg once daily (max 1000mg)", note="Take for 10 days"),
        Medication(name="Azithromycin (Zithromax)", dosage="Adult: 500mg once daily, Child: 10mg/kg on first day, then 5mg/kg for 4 days (max 500mg/day)", note="Take for 5 days"),
        Medication(name="Clarithromycin (Biaxin)", dosage="Adult: 500mg every 12 hours, Child: 15mg/kg twice daily (max 1000mg/day)", note="Take for 7-14 days"),
        Medication(name="Clindamycin", dosage="Adult: 300mg every 8 hours, Child: 8-20mg/kg/day divided into 3-4 doses", note="Take for 7-10 days"),
        Medication(name="Doxycycline", dosage="Adult: 100mg every 12 hours, Child: 50-100mg/kg/day IV or IM (max 1.5g/dose)", note="Take for 7-14 days"),
        Medication(name="Levofloxacin (Levaquin)", dosage="Adult: 500mg once daily, Child: 500mg once daily (for plague infection)", note="Take for 7-14 days"),
        Medication(name="Cefuroxime (Ceftin)", dosage="Adult: 500mg every 12 hours, Child: 250mg twice daily", note="Take for 10 days"),
        Medication(name="Epinephrine auto-injector", dosage="As directed", note="For emergency use during severe allergic reactions")
    ],
    "Flu (influenza)": [
        Medication(name="Oseltamivir (Tamiflu)", dosage="Adult: 75mg twice daily, Child: 75mg twice daily", note="Take for 5 days"),
        Medication(name="Zanamivir (Relenza)", dosage="Adult: 10mg (2 inhalations) twice daily, Child: 10mg (2 inhalations) twice daily", note="Take for 5 days"),
        Medication(name="Baloxavir marboxil (Xofluza)", dosage="Adult: 40mg (40-80kg) or 80mg (>80kg) single dose, Child: 40mg (40-80kg) or 80mg (>80kg) single dose", note="Take immediately"),
        Medication(name="Ibuprofen", dosage="200-400mg every 4-6 hours", note="Take for pain/fever relief"),
        Medication(name="Acetaminophen", dosage="325-650mg every 4-6 hours", note="Take for pain/fever relief")
    ],
    "Acute Bronchitis": [
        Medication(name="Amoxicillin", dosage="Adult: 500mg three times daily, Child: 45mg/kg/day divided into three doses", note="Take for 7-10 days"),
        Medication(name="Doxycycline", dosage="Adult: 100mg twice daily, Child: 2-4mg/kg/day divided into two doses", note="Take for 7-10 days"),
        Medication(name="Azithromycin", dosage="Adult: 500mg once daily, Child: 10mg/kg on first day, then 5mg/kg for 4 days (max 500mg/day)", note="Take for 3-5 days"),
        Medication(name="Guaifenesin", dosage="Adult: 200-400mg every 4 hours, Child: 6.25-12.5mg/kg every 4 hours", note="Take for cough/congestion relief")
    ],
    "Allergies": [
        Medication(name="Cetirizine (Zyrtec)", dosage="Adult: 10mg once daily, Child: 5-10mg once daily", note="Take as needed"),
        Medication(name="Loratadine (Claritin)", dosage="Adult: 10mg once daily, Child: 5-10mg once daily", note="Take as needed"),
        Medication(name="Fexofenadine (Allegra)", dosage="Adult: 180mg once daily, Child: 30-60mg twice daily", note="Take as needed"),
        Medication(name="Epinephrine auto-injector", dosage="As directed", note="For emergency use during severe allergic reactions")
    ],
    "Gastroenteritis": [
        Medication(name="Loperamide (Imodium)", dosage="Adult: 4mg initially, then 2mg after each loose stool (max 16mg/day), Child: 0.1-0.2mg/kg per dose", note="Take as needed"),
        Medication(name="Ondansetron (Zofran)", dosage="Adult: 4-8mg every 8 hours, Child: 0.1-0.15mg/kg every 8 hours", note="Take for nausea/vomiting"),
        Medication(name="Oral Rehydration Salts (ORS)", dosage="As directed", note="For fluid and electrolyte replacement")
    ],
    "Sinusitis": [
        Medication(name="Amoxicillin-Clavulanate", dosage="Adult: 875mg twice daily, Child: 45mg/kg/day divided into two doses", note="Take for 14 days"),
        Medication(name="Doxycycline", dosage="Adult: 100mg twice daily, Child: 2-4mg/kg/day divided into two doses", note="Take for 14 days"),
        Medication(name="Levofloxacin", dosage="Adult: 500mg once daily, Child: 500mg once daily (for plague infection)", note="Take for 14 days"),
        Medication(name="Ibuprofen", dosage="Adult: 200-400mg every 4-6 hours, Child: 10mg/kg every 6-8 hours", note="Take for pain/fever relief"),
        Medication(name="Acetaminophen", dosage="Adult: 325-650mg every 4-6 hours, Child: 10-15mg/kg every 4-6 hours", note="Take for pain/fever relief")
    ],
    "Cold": [
        Medication(name="Ibuprofen", dosage="Adult: 200-400mg every 4-6 hours, Child: 10mg/kg every 6-8 hours", note="Take for pain/fever relief"),
        Medication(name="Acetaminophen", dosage="Adult: 325-650mg every 4-6 hours, Child: 10-15mg/kg every 4-6 hours", note="Take for pain/fever relief"),
        Medication(name="Guaifenesin", dosage="Adult: 200-400mg every 4 hours, Child: 6.25-12.5mg/kg every 4 hours", note="Take for cough/congestion relief")
    ]
}




health_questions = {
    "Strep throat bacterial infection": {
        "allergic to penicillin or antibiotics": "Do you have allergic to penicillin or any other antibiotics?",
        "kidney problems": "Do you have kidney problems?",
        "respiratory infections": "Do you have respiratory infections?",
        "skin infections": "Do you have skin infections?"
    },
    "Flu (influenza)": {
        "allergic to antivirals": "Are you allergic to any antiviral medications?",
        "chronic health conditions": "Do you have any chronic health conditions (e.g., heart disease, lung disease, diabetes)?"
    },
    "Acute Bronchitis": {
        "allergic to antibiotics": "Are you allergic to any antibiotics?",
        "chronic respiratory conditions": "Do you have any chronic respiratory conditions (e.g., asthma, COPD)?"
    },
    "Allergies": {
        "taking other medications": "Are you currently taking any other medications that may interact with allergy medicines?",
        "severe allergic reactions": "Have you experienced severe allergic reactions in the past?"
    },
    "Gastroenteritis": {
        "dehydration": "Are you experiencing severe dehydration?",
        "underlying medical conditions": "Do you have any underlying medical conditions (e.g., inflammatory bowel disease, immunodeficiency)?"
    },
    "Sinusitis": {
        "allergic to antibiotics": "Are you allergic to any antibiotics?",
        "chronic sinus problems": "Do you have a history of chronic sinus problems?"
    },
    "Cold": {
        "taking other medications": "Are you currently taking any other medications that may interact with cold medicines?",
        "weakened immune system": "Do you have a weakened immune system (e.g., due to illness, medication)?"
    }
} 

symptoms = {
    "sore throat": Symptom(nom="sore throat"),
    "headache": Symptom(nom="headache"),
    "fever": Symptom(nom="fever"),
    "muscle aches": Symptom(nom="muscle aches"),
    "chills": Symptom(nom="chills"),
    "runny nose": Symptom(nom="runny nose"),
    "cough": Symptom(nom="cough"),
    "persistent cough": Symptom(nom="persistent cough"),
    "yellowish-greenish mucus": Symptom(nom="yellowish-greenish mucus"),
    "wheezing": Symptom(nom="wheezing"),
    "shortness of breath": Symptom(nom="shortness of breath"),
    "itchy sneezing": Symptom(nom="itchy sneezing"),
    "itchy eyes": Symptom(nom="itchy eyes"),
    "nausea": Symptom(nom="nausea"),
    "vomiting": Symptom(nom="vomiting"),
    "watery diarrhea": Symptom(nom="watery diarrhea"),
    "dry cough": Symptom(nom="dry cough"),
    "pain around eyes": Symptom(nom="pain around eyes"),
    "pain around cheeks": Symptom(nom="pain around cheeks"),
    "pain around nose": Symptom(nom="pain around nose"),
    "pain around forehead": Symptom(nom="pain around forehead"),
    "swellings symptoms": Symptom(nom="swellings symptoms"),
    "discharge nose": Symptom(nom="discharge nose"),
    "congestion": Symptom(nom="congestion"),
    "high fever": Symptom(nom="high fever"),
    "Sneezing": Symptom(nom="Sneezing")   
}


class DiagnosticMedical(KnowledgeEngine):

    # Rule for Strep throat bacterial infection
    @Rule(Symptom(nom="fever") &
          Symptom(nom="sore throat") &
          Symptom(nom="headache") 
          )
    def diagnostiquer_strep_throat(self):
        self.declare(Diagnosis(maladie="Strep throat bacterial infection"))
       


    # Rule for Flu (influenza)
    @Rule(Symptom(nom="fever") &
          Symptom(nom="muscle aches") &
          Symptom(nom="chills") &
          Symptom(nom="sore throat") &
          (Symptom(nom="runny nose") |
          Symptom(nom="cough")) &
          Symptom(nom="headache"))
    def diagnostiquer_flu(self):
        self.declare(Diagnosis(maladie="Flu (influenza)"))
        


    # Rule for Acute Bronchitis
    @Rule(Symptom(nom="fever") &
          Symptom(nom="persistent cough") &
          Symptom(nom="yellowish-greenish mucus") &
          Symptom(nom="wheezing") &
          Symptom(nom="shortness of breath"))
    def diagnostiquer_bronchitis(self):
        self.declare(Diagnosis(maladie="Acute Bronchitis"))



    # Rule for Allergies
    @Rule(Symptom(nom="runny nose") &
          Symptom(nom="itchy sneezing") &
          Symptom(nom="itchy eyes"))
    def diagnostiquer_allergies(self):
        self.declare(Diagnosis(maladie="Allergies"))
        


    # Rule for Gastroenteritis
    @Rule((Symptom(nom="high fever") &
          Symptom(nom="headache") &
          Symptom(nom="muscle aches") &
          Symptom(nom="nausea")) |
          (Symptom(nom="vomiting") &
          Symptom(nom="watery diarrhea")))
    def diagnostiquer_gastroenteritis(self):
        self.declare(Diagnosis(maladie="Gastroenteritis"))
        


    # Rule for Sinusitis
    @Rule(Symptom(nom="dry cough") &
          ((Symptom(nom="pain around eyes") |
          Symptom(nom="pain around cheeks") |
          Symptom(nom="pain around nose") |
          Symptom(nom="pain around forehead")) &
          Symptom(nom="swellings symptoms")) &
          Symptom(nom="headache") &
          Symptom(nom="discharge nose"))
    def diagnostiquer_sinusitis(self):
        self.declare(Diagnosis(maladie="Sinusitis"))
        


    # Rule for Cold
    @Rule(Symptom(nom="Sneezing") &
          Symptom(nom="sore throat") &
          Symptom(nom="headache") &
          Symptom(nom="congestion") &
          Symptom(nom="discharge nose"))
    def diagnostiquer_cold(self):
        self.declare(Diagnosis(maladie="Cold"))
        

    # Display the diagnosis
    @Rule(Diagnosis(maladie=MATCH.maladie))
    def display_diagnosis(self, maladie):
        st.session_state.diagnosis = maladie
        st.markdown(f"You are diagnosed with: **<span style='font-size:1.2em; color:green'>{maladie}</span>**", unsafe_allow_html=True)

    # Display the warning if diagnosis not found
    @Rule(NOT(Diagnosis()))
    def no_diagnosis_found(self):
       st.warning("No diagnosis found for the selected symptoms !")  
       st.session_state.diagnosis ="this disease is not supported !" 



class MedicationRecommendation(KnowledgeEngine):

    # Rule for Strep throat medication recommendation----------------------------------------------------------------------------------------------
    @Rule(Diagnosis(maladie="Strep throat bacterial infection") &
          TEST(lambda patient: all(response == "No" for response in patient.health_questions.values())))
    def Strep_throat_Medication_Default(self):
        for med in medications["Strep throat bacterial infection"][:-1]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    @Rule(Diagnosis(maladie="Strep throat bacterial infection") &
          TEST(lambda patient: patient.health_questions["allergic to penicillin or antibiotics"] == "Yes"))
    def Strep_throat_Medication_Antibiotic_Allergy(self):
        for med in medications["Strep throat bacterial infection"][5:]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    @Rule(Diagnosis(maladie="Strep throat bacterial infection") &
          TEST(lambda patient: patient.health_questions["kidney problems"] == "Yes"))
    def Strep_throat_Medication_Kidney_Issues(self):
        for med in medications["Strep throat bacterial infection"][1:4]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    @Rule(Diagnosis(maladie="Strep throat bacterial infection") &
          TEST(lambda patient: patient.health_questions["respiratory infections"] == "Yes"))
    def Strep_throat_Medication_Kidney_Issues(self):
        for med in medications["Strep throat bacterial infection"][4:5]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))        

    @Rule(Diagnosis(maladie="Strep throat bacterial infection") &
          TEST(lambda patient: patient.health_questions["skin infections"] == "Yes"))
    def Strep_throat_Medication_Kidney_Issues(self):
        for med in medications["Strep throat bacterial infection"][6:8]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))
            
    # Rule for Flu (Influenza) medication recommendation----------------------------------------------------------------------------------------------
    @Rule(Diagnosis(maladie="Flu (influenza)") &
          TEST(lambda patient: all(response == "No" for response in patient.health_questions.values())))
    def Flu_Medication_Default(self):
        for med in medications["Flu (influenza)"][:2]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    @Rule(Diagnosis(maladie="Flu (influenza)") &
          TEST(lambda patient: patient.health_questions["allergic to antivirals"] == "Yes"))
    def Flu_Medication_Antiviral_Allergy(self):
        self.declare(Medication(name="Ibuprofen", dosage="200-400mg every 4-6 hours", note="Take for pain/fever relief"))
        self.declare(Medication(name="Acetaminophen", dosage="325-650mg every 4-6 hours", note="Take for pain/fever relief"))

    @Rule(Diagnosis(maladie="Flu (influenza)") &
          TEST(lambda patient: patient.health_questions["chronic health conditions"] == "Yes"))
    def Flu_Medication_Chronic_Conditions(self):
        for med in medications["Flu (influenza)"][:2]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    # Rule for Acute Bronchitis medication recommendation----------------------------------------------------------------------------------------------
    @Rule(Diagnosis(maladie="Acute Bronchitis") &
          TEST(lambda patient: all(response == "No" for response in patient.health_questions.values())))
    def Acute_Bronchitis_Medication_Default(self):
        for med in medications["Acute Bronchitis"]:
            if med.name != "Amoxicillin":
                self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    @Rule(Diagnosis(maladie="Acute Bronchitis") &
          TEST(lambda patient: patient.health_questions["allergic to antibiotics"] == "Yes"))
    def Acute_Bronchitis_Medication_Antibiotic_Allergy(self):
        for med in medications["Acute Bronchitis"][3:4]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    @Rule(Diagnosis(maladie="Acute Bronchitis") &
          TEST(lambda patient: patient.health_questions["chronic respiratory conditions"] == "Yes"))
    def Acute_Bronchitis_Medication_Chronic_Respiratory(self):
        for med in medications["Acute Bronchitis"][:3]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    # Rule for Allergies medication recommendation----------------------------------------------------------------------------------------------
    @Rule(Diagnosis(maladie="Allergies") &
          TEST(lambda patient: all(response == "No" for response in patient.health_questions.values())))
    def Allergies_Medication_Default(self):
        for med in medications["Allergies"][:2]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    @Rule(Diagnosis(maladie="Allergies") &
          TEST(lambda patient: patient.health_questions["severe allergic reactions"] == "Yes"))
    def Allergies_Medication_Severe_Reactions(self):
        self.declare(Medication(name=medications["Allergies"][3].name, dosage=medications["Allergies"][3].dosage, note=medications["Allergies"][3].note))

    @Rule(Diagnosis(maladie="Allergies") &
          TEST(lambda patient: patient.health_questions["taking other medications"] == "Yes"))
    def Allergies_Medication_Other_Meds(self):
        for med in medications["Allergies"][:3]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    # Rule for Gastroenteritis medication recommendation----------------------------------------------------------------------------------------------
    @Rule(Diagnosis(maladie="Gastroenteritis") &
          TEST(lambda patient: all(response == "No" for response in patient.health_questions.values())))
    def Gastroenteritis_Medication_Default(self):
        for med in medications["Gastroenteritis"][:3]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    @Rule(Diagnosis(maladie="Gastroenteritis") &
          TEST(lambda patient: patient.health_questions["dehydration"] == "Yes"))
    def Gastroenteritis_Medication_Dehydration(self):
        self.declare(Medication(name="Oral Rehydration Salts (ORS)", dosage="As directed", note="For fluid and electrolyte replacement"))

    @Rule(Diagnosis(maladie="Gastroenteritis") &
          TEST(lambda patient: patient.health_questions["underlying medical conditions"] == "Yes"))
    def Gastroenteritis_Medication_Underlying_Conditions(self):
        for med in medications["Gastroenteritis"]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    # Rule for Sinusitis medication recommendation----------------------------------------------------------------------------------------------
    @Rule(Diagnosis(maladie="Sinusitis") &
          TEST(lambda patient: all(response == "No" for response in patient.health_questions.values())))
    def Sinusitis_Medication_Default(self):
        for med in medications["Sinusitis"][:-1]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    @Rule(Diagnosis(maladie="Sinusitis") &
          TEST(lambda patient: patient.health_questions["allergic to antibiotics"] == "Yes"))
    def Sinusitis_Medication_Antibiotic_Allergy(self):
        for med in medications["Sinusitis"][3:5]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    @Rule(Diagnosis(maladie="Sinusitis") &
          TEST(lambda patient: patient.health_questions["chronic sinus problems"] == "Yes"))
    def Sinusitis_Medication_Chronic_Sinus(self):
        for med in medications["Sinusitis"][:3]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    # Rule for Cold medication recommendation----------------------------------------------------------------------------------------------
    @Rule(Diagnosis(maladie="Cold") &
          TEST(lambda patient: all(response == "No" for response in patient.health_questions.values())))
    def Cold_Medication_Default(self):
        for med in medications["Cold"][:3]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    @Rule(Diagnosis(maladie="Cold") &
          TEST(lambda patient: patient.health_questions["taking other medications"] == "Yes"))
    def Cold_Medication_Other_Meds(self):
        self.declare(Medication(name=medications["Cold"][2].name, dosage=medications["Cold"][2].dosage, note=medications["Cold"][2].note))

    @Rule(Diagnosis(maladie="Cold") &
          TEST(lambda patient: patient.health_questions["weakened immune system"] == "Yes"))
    def Cold_Medication_Weakened_Immune(self):
        for med in medications["Cold"]:
            self.declare(Medication(name=med.name, dosage=med.dosage, note=med.note))

    # Display medications recommendation----------------------------------------------------------------------------------------------
    @Rule(Medication(name=MATCH.name, dosage=MATCH.dosage, note=MATCH.note))
    def display_medications_recommendation(self, name, dosage, note):
    
        # Split the dosage string into "Adult:" and "Child:" parts
        dosage_parts = dosage.split(",")
        adult_dosage = None
        child_dosage = None
        for part in dosage_parts:
            if "Adult:" in part:
                adult_dosage = part.strip("Adult: ")
            elif "Child:" in part:
                child_dosage = part.strip("Child: ")

        # Check the patient's age
        if PatientInformation(age=P(lambda value: value >= 18)):
            # Display the medication for adult patients
            st.write(f"We recommend: {name} - Dosage: {adult_dosage} - Note: {note}")
        else:
            # Calculate the new dosage for child patients based on their weight
            child_dosage_value = float(child_dosage.split(" ")[0])
            child_dosage_unit = child_dosage.split(" ")[1]
            new_dosage = str(child_dosage_value * PatientInformation(weight=P(lambda value: value))) + " " + child_dosage_unit
            # Display the medication for child patients
            st.write(f"We recommend: {name} - Dosage: {new_dosage} - Note: {note}")

    # If no medications recommendation is found----------------------------------------------------------------------------------------------
    @Rule(NOT(Medication()))
    def no_medications_recommendation_found(self):
        st.warning("No medications can be recommended!")


    
def main(): 

    st.title("welcome to Cold and Flu Diagnostic")
   
    # Initialize the Diagnostic Medical engine
    diagnosis_engine = DiagnosticMedical()

   # Create a multiselect component for symptoms
    st.subheader('Select your symptoms 🩺', divider='blue')
    st.session_state.selected_symptoms = st.multiselect(' ', list(symptoms.keys()))

    # Button to trigger diagnosis
    if button("Diagnose" , key="start_diagnosis"):
        # Reset the engine and declare selected symptoms
        diagnosis_engine.reset()
        for symptom in st.session_state.selected_symptoms:
            diagnosis_engine.declare(symptoms[symptom])
        # Run the engine
        diagnosis_engine.run()

        #medications recommendation section  
        if button("Next" , key="start_medications_recommendation") :

            st.subheader('Medications recommendation 💊', divider='blue')

            # overall health questions for the curent diagnosis:
            diagnosis = st.session_state.diagnosis  
            if diagnosis in health_questions:
                st.session_state.responses = {}

               # Initialize the Medications Recommendation engine
                medication_engine = MedicationRecommendation()

                #sliders for weight and age
                st.session_state.age = int(st.slider("What is your age?", 2, 100))
                st.session_state.weight = int(st.slider("What is your weight (in kg)?", 10, 200))


                for question in health_questions[diagnosis]:
                    st.session_state.responses[question] = st.radio(health_questions[diagnosis][question], ("Yes", "No"))
                
                if button("see medications" , key="display_medications"):
                    # Reset the engine and declare selected responses
                    medication_engine.reset()
                    medication_engine.declare(PatientInformation(age=st.session_state.age, weight=st.session_state.weight, health_questions=st.session_state.responses))
                    medication_engine.run()
                    
                    #indication
                    with bottom():
                        st.info("The diagnostic completely depends on your inputs. Please double-check responses.")
            else :
                st.warning("There is a problem with the diagnostic results. Please reselect only the correct symptoms.")
                
            
if __name__ == "__main__":
    main()