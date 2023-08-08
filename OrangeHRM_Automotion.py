from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class OrangeHRM():

    def website(self):
        driver=webdriver.Chrome(executable_path="E:\AutomationBITM06\Drivers\Drivers\chromedriver_102.0.exe")
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")

#find website title
        title=driver.title
        original_title= "OrangeHRM"
        if original_title == title:
            print("Title matched")
        else:
            print("Title Not matched")

     # Print the title
        if title is not None:
            print ("the titele is" ,title )
        else:
            print("not found")

#find url
        url=driver.current_url
        print("the current url :",url )

#find username/password element
        username = driver.find_element(By.ID, "txtUsername")
        if username is not None:
            print("User Name Element found")
        else:
            print("not found")

        password= driver.find_element(By.ID,"txtPassword")
        if password is not None:
            print("Password Element found")
        else:
            print("not found")

        login_btn = driver.find_element(By.ID,"btnLogin")
        if login_btn is not None:
            print ("login button found")
        else:
            print("not found")

# enter value and click
        username.clear()
        username.send_keys("Admin")
        password.clear()
        password.send_keys("admin123")

# click method
        login_btn.click()

# find element myinfo

        myinfo = driver.find_element(By.XPATH, '//*[@id="menu_pim_viewMyDetails"]/b')
        if myinfo is not None:
            print("My Info sub menu found ")
        else:
            print("MY Info Not found ")
#click
        myinfo.click()

#find edit button

        editbtn=driver.find_element(By.XPATH, '//*[@id="btnSave"]')
        if editbtn is not None:
            print("Edit button found")
        else:
            print("Edit Button not found")

#click edit button
        editbtn.click()

# find element in myinfo page
        fullname=driver.find_element(By.XPATH,'//*[@id="frmEmpPersonalDetails"]/fieldset/ol[1]/li/label')
        if fullname is not None:
            print("Full Name element found")
        else:
            print("Full Name element not found")

        fname=driver.find_element(By.XPATH, '//*[@id="personal_txtEmpFirstName"]')  #find first name
        if fname is not None:
            print("First Name element found")
        else:
            print("First Name element not found")

        fname.clear()
        fname.send_keys("Saim")

        m_name=driver.find_element(By.XPATH,'//*[@id="personal_txtEmpMiddleName"]')
        if fname is not None:
            print("Middle Name element found")
        else:
            print("Middle Name element not found")

        m_name.clear()
        m_name.send_keys("kabir")

        l_name=driver.find_element(By.XPATH,'//*[@id="personal_txtEmpLastName"]')
        if l_name is not None:
            print("Last Name element found")
        else:
            print("Last Name element not found")

        l_name.clear()
        l_name.send_keys("Joy")



#find Employee Id Element
        employeeId= driver.find_element(By.XPATH, '// *[ @ id = "frmEmpPersonalDetails"] / fieldset / ol[2] / li[1] / label')
        if employeeId is not None:
            print("Employee Id  found")
        else:
            print("Employee Id not found")

        emp_idfield= driver.find_element(By.ID,"personal_txtEmployeeId")
        if emp_idfield is not None:
            print("Employee Id Field found")
        else:
            print("Employee Id Field not found")

        emp_idfield.clear()
        emp_idfield.send_keys("Emp012")

        other_id=driver.find_element(By.XPATH, '//*[@id="personal_txtOtherID"]')
        if other_id is not None:
            print("Other Id Field Element")
        else:
            print("Other Id Field not found")

        drive_license=driver.find_element(By.ID,"personal_txtLicenNo")
        if drive_license is not None:
            print("Driver License Field found")
        else:
            print("Driver License Field found")

        drive_license.clear()
        drive_license.send_keys("Driver-0123")

# License expire date
        license_expdate=driver.find_element(By.XPATH, '//*[@id="personal_txtLicExpDate"]')
        if license_expdate is not None:
            print("Date picker Element found")
        else:
            print("Date picker element not found")

        license_expdate.clear()
        time.sleep(3)
        license_expdate.send_keys("2022-06-08")

#SSN Number

     #   ssn_number=driver.find_element(By.XPATH,'//*[@id="personal_txtNICNo"]')
     #   ssn_number.clear()
     #   ssn_number.send_keys("607-66-XXXX")
    #    if ssn_number is not None:
            #print("SSN Element found")
    #    else:
         #   print("SSN not found")

#SIN Number
     #   sin_num=driver.find_element(By.XPATH,'//*[@id="personal_txtSINNo"]')
       # sin_num.clear()
     #   sin_num.send_keys("665-56-yXXX")
     #   if sin_num is not None:
     #       print("Sin_num element found")
     #   else:
    #        print("Sin_num element Not found")

#gender Element
        #male=driver.find_element(By.XPATH,'//*[@id="frmEmpPersonalDetails"]/fieldset/ol[3]/li[1]/ul/li[1]/label')
        #male.click()
        #male_btn_status = male.is_selected()   #for checiking the button status it is selected or not
       # time.sleep(5)

        female=driver.find_element(By.XPATH,'//*[@id="frmEmpPersonalDetails"]/fieldset/ol[3]/li[1]/ul/li[2]/label')
        female.click()
        time.sleep(3)

#Dropdown
        maritial_status= driver.find_element(By.XPATH,'//*[@id="personal_cmbMarital"]')
        m_dropdown= Select(maritial_status)
        m_dropdown.select_by_value('Single')
        time.sleep(3)

#Nationality
        n_status= driver.find_element(By.XPATH,'//*[@id="personal_cmbNation"]')
        n_dropdwon=Select(n_status)
        n_dropdwon.select_by_value('15')
        time.sleep(3)

#dob
        d_birth=driver.find_element(By.XPATH,'//*[@id="personal_DOB"]')
        d_birth.clear()
        d_birth.send_keys('1997-04-05')
        time.sleep(2)
#nickname
      #  nick_name = driver.find_element(By.XPATH,'//*[@id="personal_txtEmpNickName"]')
      #  nick_name.clear()
     #   nick_name.send_keys("saim")
      #  time.sleep(2)
#somker status
      #  smoker_flag = driver.find_element(By.XPATH,'//*[@id="personal_chkSmokeFlag"]')
      #  if smoker_flag is not None:
     #       print("Smoker flag element found")
      #  else:
       #     print("Smoker Element Not found")

#save btn
        save_btn=driver.find_element(By.XPATH,'//*[@id="btnSave"]')
        save_btn.click()
        time.sleep(2)  #freez window

#Custom field

        edit_btn=driver.find_element(By.XPATH, '//*[@id="btnEditCustom"]')
        edit_btn.click()

        blood_type=driver.find_element(By.XPATH,'//*[@id="frmEmpCustomFields"]/ol/li[1]/select')
        blood_type_dropdown=Select(blood_type)
        blood_type_dropdown.select_by_value("O+")
        time.sleep(2)

      # extra_field=driver.find_element(By.XPATH,'//*[@id="custom2"]')
      #  extra_field.clear()
       # extra_field.send_keys("Uni-Donar")

        save_btn2=driver.find_element(By.XPATH,'//*[@id="btnEditCustom"]')
        save_btn2.click()
        time.sleep(2)
#Attachment  filed
        add_btn= driver.find_element(By.XPATH, '//*[@id="btnAddAttachment"]')
        add_btn.click()

        choose_btn= driver.find_element(By.XPATH,'//*[@id="ufile"]')
        choose_btn.click()
        choose_btn.send_keys('//*[@id="ufile"]')
        comment_box=driver.find_element(By.XPATH,'//*[@id="txtAttDesc"]')
        comment_box.send_keys("asdfds")
        upload_button=driver.find_element(By.XPATH,'//*[@id="btnSaveAttachment"]')
        upload_button.click()
        time.sleep(3)

test_obj = OrangeHRM()
test_obj.website()