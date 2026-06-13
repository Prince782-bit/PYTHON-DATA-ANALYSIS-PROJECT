import streamlit as st
import mysql.connector

st.set_page_config(page_title="Hospital Management System")
st.title("🏥 Hospital Management System")


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pyadav001",
    database="mydata",
    port=3306
)

print("Connection Successful!")

c = conn.cursor()




# ---------------- SIDEBAR MENU ----------------
menu = st.sidebar.selectbox(
    "Menu",
    ["Add Patient", "View Patients", "Update Patient", "Delete Patient"]
)

# ---------------- ADD PATIENT ----------------
if menu == "Add Patient":

    st.subheader("Add Patient Details")

    Nameoftablets = st.text_input("Name of Tablets")
    ref = st.text_input("Reference No")
    Dose = st.text_input("Dose")
    NumberofTablets = st.text_input("Number of Tablets")
    Lot = st.text_input("Lot")
    Issuedate = st.text_input("Issue Date")
    ExpDate = st.text_input("Expiry Date")
    DailyDose = st.text_input("Daily Dose")
    sideEfect = st.text_input("Side Effect")
    FurtherInformation = st.text_input("Further Information")
    StorageAdvice = st.text_input("Storage Advice")
    DrivingUsingMachine = st.text_input("Blood Pressure")
    HowToUseMedication = st.text_input("Medication Usage")
    PatientId = st.text_input("Patient ID")
    nhsNumber = st.text_input("NHS Number")
    PatientName = st.text_input("Patient Name")
    DateOfBirth = st.text_input("Date of Birth")
    PatientAddress = st.text_input("Patient Address")

    if st.button("Save Patient"):

        try:
            c.execute("""
                INSERT INTO hospital (
                Nameoftablets, ref, Dose, NumberofTablets, Lot,
                Issuedate, ExpDate, DailyDose, sideEfect,
                FurtherInformation, StorageAdvice, DrivingUsingMachine,
                HowToUseMedication, PatientId, nhsNumber,
                PatientName, DateOfBirth, PatientAddress
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                Nameoftablets, ref, Dose, NumberofTablets, Lot,
                Issuedate, ExpDate, DailyDose, sideEfect,
                FurtherInformation, StorageAdvice, DrivingUsingMachine,
                HowToUseMedication, PatientId, nhsNumber,
                PatientName, DateOfBirth, PatientAddress
            ))

            conn.commit()
            st.success("Patient Added Successfully ✔️")

        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- VIEW PATIENTS ----------------
elif menu == "View Patients":
    st.subheader("All Patients Data")

    c.execute("SELECT * FROM hospital")
    data = c.fetchall()

    if len(data) == 0:
        st.warning("No records found")

    else:
        import pandas as pd

        # 👉 column names fetch karo
        column_names = [desc[0] for desc in c.description]

        # 👉 dataframe with proper headers
        df = pd.DataFrame(data, columns=column_names)

        st.dataframe(df)





elif menu == "Update Patient":
    st.subheader("Update Patient Details")

    ref = st.text_input("Enter Reference No (Required)")

    st.markdown("### Fill only fields you want to update")

    Nameoftablets = st.text_input("Name of Tablets")
    Dose = st.text_input("Dose")
    NumberofTablets = st.text_input("Number of Tablets")
    Lot = st.text_input("Lot")
    Issuedate = st.text_input("Issue Date")
    ExpDate = st.text_input("Expiry Date")
    DailyDose = st.text_input("Daily Dose")
    sideEfect = st.text_input("Side Effect")
    FurtherInformation = st.text_input("Further Information")
    StorageAdvice = st.text_input("Storage Advice")
    DrivingUsingMachine = st.text_input("Blood Pressure")
    HowToUseMedication = st.text_input("Medication")
    PatientId = st.text_input("Patient ID")
    nhsNumber = st.text_input("NHS Number")
    PatientName = st.text_input("Patient Name")
    DateOfBirth = st.text_input("DOB")
    PatientAddress = st.text_input("Address")

    if st.button("Update Patient"):

        if ref == "":
            st.error("Reference No is required")

        else:
            updates = {}
            values = []

            if Nameoftablets: updates["Nameoftablets"] = Nameoftablets
            if Dose: updates["Dose"] = Dose
            if NumberofTablets: updates["NumberofTablets"] = NumberofTablets
            if Lot: updates["Lot"] = Lot
            if Issuedate: updates["Issuedate"] = Issuedate
            if ExpDate: updates["ExpDate"] = ExpDate
            if DailyDose: updates["DailyDose"] = DailyDose
            if sideEfect: updates["sideEfect"] = sideEfect
            if FurtherInformation: updates["FurtherInformation"] = FurtherInformation
            if StorageAdvice: updates["StorageAdvice"] = StorageAdvice
            if DrivingUsingMachine: updates["DrivingUsingMachine"] = DrivingUsingMachine
            if HowToUseMedication: updates["HowToUseMedication"] = HowToUseMedication
            if PatientId: updates["PatientId"] = PatientId
            if nhsNumber: updates["nhsNumber"] = nhsNumber
            if PatientName: updates["PatientName"] = PatientName
            if DateOfBirth: updates["DateOfBirth"] = DateOfBirth
            if PatientAddress: updates["PatientAddress"] = PatientAddress

            if len(updates) == 0:
                st.warning("Koi field fill nahi kiya update ke liye")

            else:
                query = "UPDATE hospital SET "
                
                for key, value in updates.items():
                    query += f"{key}=%s, "
                    values.append(value)

                query = query.rstrip(", ")
                query += " WHERE ref=%s"
                values.append(ref)

                c.execute(query, tuple(values))
                conn.commit()

                st.success("Patient Updated Successfully (Only filled fields updated)")










elif menu == "Delete Patient":
    st.subheader("Delete Patient Record")

    ref = st.text_input("Enter Reference No to Delete")

    if st.button("Delete Patient"):

        if ref.strip() == "":
            st.error("Please enter Reference Number")
        else:
            try:
                sql = "DELETE FROM hospital WHERE ref=%s"
                c.execute(sql, (ref,))   # 🔥 IMPORTANT: comma must be here
                conn.commit()

                if c.rowcount == 0:
                    st.warning("No record found with this Reference No")
                else:
                    st.success("Patient Deleted Successfully")

            except Exception as e:
                st.error(f"Error: {e}")













# run the app
# cd "PYTHON-DATA-ANALYSIS-PROJECT\Hospital Management System"
# python -m streamlit run app.py