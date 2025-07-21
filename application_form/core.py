def my_form():
    form_data={
        "name":input("Enter the name of the applicant:"),
        "age":int(input("Enter the age of the applicant:")),
        "gender":input("Enter the Gender(Male/Female/others):"),
        "dob":input("Enter the Date of Birth (dd/mm/yyyy):"),
        "course":input("Enter the Course you were intrested:"),
        "f_name":input("Enter the Father name:"),
        "m_name":input("Enter the Mother name:"),
        "adrs":input("Enter the address:")
    }
    
    return form_data

