from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
import json

# Ruta al archivo JSON con los datos
data_file_path = r'C:\Users\deivi\OneDrive\Documents\CursoA\CursoA-FullStack\data1.json'

# Leer datos del archivo JSON
with open(data_file_path, 'r') as f:
    data = json.load(f)

emails = data['emails']
passwords = data['passwords']
first_names = data['first_names']
last_names = data['last_names']
birthdates = data['birthdates']
cities = data['cities']
states = data['states']
zip_codes = data['zip_codes']

# Ruta al ejecutable de Firefox Portable
firefox_portable_path = r'C:\Users\deivi\OneDrive\Desktop\creacion de cuentas\pruebas\App\Firefox\firefox.exe'

# Ruta al perfil de Firefox Portable
firefox_profile_path = r'C:\Users\deivi\OneDrive\Desktop\creacion de cuentas\pruebas\Data\profile'

# Configuración del navegador Firefox
options = Options()
options.binary_location = firefox_portable_path

# Crear una instancia del perfil de Firefox
profile = webdriver.FirefoxProfile(firefox_profile_path)
options.profile = profile

# Ruta al geckodriver
geckodriver_path = r'C:\Users\deivi\Downloads\geckodriver\geckodriver.exe'

# Crear una instancia del controlador de Firefox con el perfil
driver = webdriver.Firefox(service=Service(geckodriver_path), options=options)

# URL de la página de registro
url = 'https://crowdtap.com/auth/account-creation-email'

# Tomar el primer valor de cada lista
email = emails[0]
password = passwords[0]
first_name = first_names[0]
last_name = last_names[0]
birthdate = birthdates[0]
city = cities[0]
state = states[0]
zip_code = zip_codes[0]

try:
    time.sleep(8)
    # Abrir la página de registro
    driver.get(url)

    # Esperar a que los elementos de la página se carguen
    wait = WebDriverWait(driver, 3)

    # Paso 1: Registro de correo electrónico y contraseña
    email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="email"]')))
    password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]')))
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-track="member-sign-up-continue"]')))

    email_field.send_keys(email)
    password_field.send_keys(password)
    submit_button.click()
    print("Paso 1 completado")

    time.sleep(7)

    # Paso 2: Completar nombre y apellido
    firstname_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="first_name"]')))
    print("Nombre Listo")
    lastname_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="last_name"]')))
    print("Apellido Listo")
    next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-track="member-sign-up-continue"]')))

    firstname_field.send_keys(first_name)
    lastname_field.send_keys(last_name)
    next_button.click()
    print("Paso 2 completado")

    time.sleep(3)
    
    # Paso 3: Completar fecha de nacimiento y seleccionar género y etnicidad
    birthdate_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="birthdate"]')))
    gender_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select[formcontrolname="gender"]')))
    ethnicity_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select[formcontrolname="ethnicity_id"]')))
    next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-track="member-sign-up-continue"]')))

    birthdate_field.send_keys(birthdate)
    
    # Seleccionar género
    #select_gender = Select(gender_select)
    #select_gender.select_by_visible_text('Female')  # Selecciona 'Male' del dropdown

    # Seleccionar etnicidad
    select_ethnicity = Select(ethnicity_select)
    select_ethnicity.select_by_visible_text('White / Caucasian')  # Selecciona 'White' del dropdown

    next_button.click()
    print("Paso 3 completado")

    time.sleep(3)
    
    # Paso 4: Completar ciudad, estado y código postal
    city_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="city"]')))
    state_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select[formcontrolname="state_id"]')))
    zip_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="zip_code"]')))
    finish_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-track="reg2-btn-finish"]')))

    city_field.send_keys(city)
    
    # Seleccionar estado
    select_state = Select(state_select)
    select_state.select_by_visible_text(state)  # Selecciona 'New York' del dropdown

    zip_field.send_keys(zip_code)

    # Localizar el checkbox y hacerle click
    checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='check-1']")))
    checkbox.click()
    print("Checkbox seleccionado")

    finish_button.click()
    print("Paso 4 completado")

    print("Registro completado con éxito")
    
    # Eliminar el primer valor de cada lista después de completar el registro
    emails.pop(0)
    passwords.pop(0)
    first_names.pop(0)
    last_names.pop(0)
    birthdates.pop(0)
    cities.pop(0)
    states.pop(0)
    zip_codes.pop(0)
    
    print("eliminado el primer valor de cada lista")
    
    # Guardar las listas actualizadas en el archivo JSON para futuras ejecuciones
    data = {
        'emails': emails,
        'passwords': passwords,
        'first_names': first_names,
        'last_names': last_names,
        'birthdates': birthdates,
        'cities': cities,
        'states': states,
        'zip_codes': zip_codes
    }
    print("guardando las listas actualizadas en el archivo JSON")
    
    with open(data_file_path, 'w') as f:
        json.dump(data, f)

except TimeoutException as e:
    print("Error: Elemento no encontrado o tiempo de espera excedido", e)
except NoSuchElementException as e:
    print("Error: Elemento no encontrado", e)
#finally:
    # Cerrar el navegador
    #driver.quit()
