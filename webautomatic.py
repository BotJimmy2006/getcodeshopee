"""

  #### 2022 - 2024 เขียนโค้ดง่ายนิดเดียว , © All Right Reserved ####
  #### 2022 - 2024 เขียนโค้ดง่ายนิดเดียว , © All Right Reserved ####
  #### 2022 - 2024 เขียนโค้ดง่ายนิดเดียว , © All Right Reserved ####

  เวอร์ชั่น 2.2 / 05-07-2024

"""

import sys ; import importlib ; import importlib.util ; import os ; import psutil ; module = importlib.import_module( f'module.WAMT_PY{sys.version_info.major}{sys.version_info.minor}.WAMT_PY{sys.version_info.major}{sys.version_info.minor}' ) ; O0OOO0O0O0OO00OOO = getattr(module, 'O0OOO0O0O0OO00OOO');OOOO00O000OO0O0OO = getattr(module, 'OOOO00O000OO0O0OO');OO0O0OOO0000O00O0 = getattr(module, 'OO0O0OOO0000O00O0');
import requests ; import undetected_chromedriver as uc; from selenium.webdriver.common.action_chains import ActionChains;from selenium.webdriver.support.ui import WebDriverWait;from selenium.webdriver.common.keys import Keys;from selenium.webdriver.support import expected_conditions as EC;import time ,win32clipboard ,pyperclip , codecs , zipfile , shutil , os , logging , json ;from datetime import datetime ;from PIL import Image ;from io import BytesIO ;import chromedriver_autoinstaller;import chrome_version;from selenium.common.exceptions import WebDriverException;import tempfile , urllib , urllib.error , urllib.request;from selenium_authenticated_proxy import SeleniumAuthenticatedProxy;import xml.etree.ElementTree as elemTree;import base64;import io;

class tool :

  # --- เปิด Chrome
  def open_web_chrome (part_profile , delay_web=5 , show_img=True , headless_windows=False , extension =[] , load_extensions_name = []  , proxy = [] , browser_executable_path_setup = None , driver_executable_path_setup = None , version_main_setup = None ,  user_multi_procs_setup = False ,  add_argument_custom=[] , showdb=True ) :
    
    """
    เปิด Chrome Selenuim.s

    พารามิเตอร์:
      - part_profile (str): ตำแหน่งที่เก็บโฟรเดอร์โปรไฟล์ Chrome
      - delay_web (int): วินาทีในการรอโหลด Element ทั้งหมด (default เป็น 5)
      - show_img (bool): Load ภาพหน้าเว็บหรือไม่ (default เป็น True)
      - headless_windows (bool): โหมด Chrome ทำงาน Chrome เบื้องหลัง (default เป็น False)
      - extension (list): extension Chrome ที่ต้องการติดตั้ง (default เป็น [])
      - load_extensions_name (list): ชื่อ extensions ที่ต้องการโหลด (default เป็น [])
      - proxy (list): Proxy ที่ต้องการใช้งาน (default เป็น [])
      - browser_executable_path_setup (str): ตำแหน่งของไฟล์ chrome.exe (default เป็น None)
      - driver_executable_path_setup (str): ตำแหน่งของไฟล์ chromedriver.exe (default เป็น None)
      - version_main_setup (str): เวอร์ชั่นของตัว Chrome (default เป็น None)
      - user_multi_procs_setup (bool): เร่งความเร็ว Chrome ด้วย multi_procs (default เป็น False)
      - add_argument_custom (list): เพิ่ม argument ที่ต้องการ (default เป็น [])
      - showdb (bool): แสดงการทำงานของ Code (default เป็น True)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องการคืนค่าออกมาเป็น อ็อบเจ็กต์ของ selenium.webdriver ที่ใช้ในการควบคุมเบราว์เซอร์
    """

    return OOOO00O000OO0O0OO.O00O0O000OO0OOOO0 (part_profile , delay_web, show_img, headless_windows, extension , load_extensions_name , proxy , browser_executable_path_setup , driver_executable_path_setup , version_main_setup , user_multi_procs_setup , add_argument_custom , showdb )

  # --- ดึงข้อมูล WebDrive
  def find_chrome( versions_selete ) :

    """
    ดึงข้อมูลลิงค์ดาวน์โหลด ChromeDriver

    พารามิเตอร์:
      - versions_selete (str): ค่าเวอร์ชั่นของ Chrome

    ผลลัพธ์:
      - ถ้ามีข้อมูลจะคืนค่าออกมาเป็นลิงค์ดาวน์โหลด
    """

    export = []
    data = requests.get( 'https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json' )
    if data.status_code == 200 :
      data = json.loads( data.text )
      for var in data['versions'] :
        if str( var['version'] ).find( versions_selete ) != -1 :
          export.append( var )

    for var in export :
      print( 'Version : ' , var['version'] )
      print( '='*10 , ' Chrome ' , '='*10  )
      for var2 in var['downloads']['chrome']  :
        print(var2  )
      print( '='*10 , ' Chromedriver ' , '='*10  )
      for var2 in var['downloads']['chromedriver']  :
        print(var2  )
      print( '\n' )

  # --- แสดงข้อมูล attribute จ่าก element
  def print_attribute ( element_data , attribute , print_all=True , showdb=False ) :

    """
    แสดงข้อมูลจาก attribute ของอ็อบเจ็กต์ element.

    พารามิเตอร์:
      - element_data (selenium.webdriver.remote.webelement.WebElement): Object Element ของ Selenuim
      - attribute (str): attribute ที่ต้องการดึงข้อมูล
      - print_all (bool): กำหนดให้เป็น True เพื่อแสดงข้อมูลทั้งหมด หรือเป็น False เพื่อไม่แสดงข้อมูล
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้า Error จะคีนค่า False
    """

    return OOOO00O000OO0O0OO.OOO0000O0OOOO00OO (element_data , attribute , print_all, showdb )

  # --- แสดงข้อมูล text จ่าก element
  def print_text ( element_data , print_all=True , showdb=False ) :

    """
    แสดงข้อมูลจากข้อความในอ็อบเจ็กต์ element.

    พารามิเตอร์:
      - element_data (selenium.webdriver.remote.webelement.WebElement): Object Element ของ Selenuim
      - print_all (bool): กำหนดให้เป็น True เพื่อแสดงข้อมูลทั้งหมด หรือเป็น False เพื่อไม่แสดงข้อมูล
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้า Error จะคีนค่า False
    """

    return OOOO00O000OO0O0OO.O0O000000000O0OO0 (element_data , print_all, showdb )

  # --- แปลงข้อมูล attribute  จ่าก element เป็น list
  def convert_attribute_to_list ( element_data , attribute  , showdb=False ):

    """
    แปลงข้อมูลจาก attribute ของอ็อบเจ็กต์ element เป็นรายการ (list).

    พารามิเตอร์:
      - element_data (selenium.webdriver.remote.webelement.WebElement): Object Element ของ Selenuim
      - attribute (str): attribute ที่ต้องการดึงข้อมูล
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น List[]
      - ถ้า Error จะคีนค่า False
    """

    return OOOO00O000OO0O0OO.OO0OOO0OOO0000O00 ( element_data , attribute , showdb )
  
  # --- แปลงข้อมูล text  จ่าก element เป็น list
  def convert_text_to_list ( element_data  , showdb=False ):

    """
    แปลงข้อมูลจากข้อความในอ็อบเจ็กต์ element เป็นรายการ (list).

    พารามิเตอร์:
      - element_data (selenium.webdriver.remote.webelement.WebElement): Object Element ของ Selenuim
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น List[]
      - ถ้า Error จะคีนค่า False
    """

    return OOOO00O000OO0O0OO.OO00OO00O000O0OO0 ( element_data , showdb )

  # --- เลื่อนสกอบาร์ไม่จำกัด
  def infinite_scroll_bar( driver , wait_to_load=3 , timeout=5 , showdb=False ) :

    """
    เลื่อนสกอบาร์เลื่อยๆตามเวลาที่กำหนด

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - wait_to_load (int): ระยะเวลาในการหยุดการเลื่อนก่อนจะโหลดเพิ่มเติม (หน่วย: วินาที) (default เป็น 3)
      - timeout (int): ระยะเวลาที่จะเลื่อนสกอบาร์ทั้งหมด (หน่วย: วินาที) (default เป็น 5)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคีนค่า False
    """
    return OOOO00O000OO0O0OO.O000O00OO0O0O0O0O(driver , wait_to_load, timeout, showdb)

  # --- ดึงความสูงสกอบาร์
  def get_scroll_height( driver , showdb=False ) :

    """
    ดึงความสูงของสกอร์บาร์.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็นความสูงของหน้าต่าง int()
      - ถ้า Error จะคีนค่า False
    """

    return OOOO00O000OO0O0OO.O000O0O0000O0O000( driver, showdb )

class webautomatic :

  # --- เข้าหน้าเว็บ
  def goto_web( driver , url , clear_ctrl_f5=False , wait_to_load=5  , showdb=False ) :

    """
    ไปยังหน้าเว็บที่ระบุด้วย URL.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - url (str): URL ของหน้าเว็บที่ต้องการเข้าไป
      - clear_ctrl_f5 (bool): กำหนดให้เป็น True เพื่อล้างแคชและโหลดหน้าเว็บใหม่โดยใช้ Ctrl + F5 หรือเป็น False หากไม่ต้องการ (default เป็น False)
      - wait_to_load (int): เวลาที่รอให้หน้าเว็บโหลดเสร็จสิ้นหลังจากเข้าไป (เป็นจำนวนวินาที, default เป็น 5)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคีนค่า False
    """

    return O0OOO0O0O0OO00OOO.O0O000O00OOOO0OO0(driver , url , clear_ctrl_f5, wait_to_load ,showdb )
  
  # --- ค้นหา Text
  def find_text_by_xpath (driver ,text ,timeout =0.5 ,tag =['div','span','a','button'] , mark=True , showdb=False ):
    
    """
    ค้นหาข้อความบนหน้าเว็บด้วย XPath ในแท็กที่ระบุ.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - text (str): ข้อความที่ต้องการค้นหาในหน้าเว็บ
      - timeout (float): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - tag (list[str,,]): รายการแท็กที่ต้องการค้นหา (default เป็น ['div', 'span', 'a', 'button'])
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าเจอ Tag ที่ต้องการจะคืนออกมาเป็น อ็อบเจ็กต์ selenium.webdriver.remote.webelement.WebElement
      - ถ้าไม่เจอ Tag จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.O0000OO0O0O00OOO0 (driver ,text ,timeout ,tag , mark , showdb )

  # --- ค้นหา Text หลายตำแหน่ง
  def find_text_by_xpath_muti (driver ,text ,timeout =0.5 ,tag =['div','span','a','button'] , mark=True , showdb=False  ):

    """
    ค้นหาข้อความบนหน้าเว็บด้วย XPath ในแท็กที่ระบุ.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - text (str): ข้อความที่ต้องการค้นหาในหน้าเว็บ
      - timeout (float): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - tag (list[str,,]): รายการแท็กที่ต้องการค้นหา (default เป็น ['div', 'span', 'a', 'button'])
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าเจอ Tag ที่ต้องการจะคืนออกมาเป็น อ็อบเจ็กต์รูปแบบ List [selenium.webdriver.remote.webelement.WebElement]
      - ถ้าไม่เจอ Tag จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.OOO0OOOOO0OOO000O (driver ,text ,timeout ,tag , mark , showdb  )

  # --- ค้นหา Text แบบ contains
  def find_text_contains_by_xpath ( driver , text , timeout=0.5 , tag=['div','span','a','button'] , mark=True , showdb=False  ):

    """
    ค้นหาข้อความบนหน้าเว็บด้วย XPath ในแท็กที่ระบุ ( ค้นหาแบบ contains ).

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - text (str): ข้อความที่ต้องการค้นหาในหน้าเว็บ
      - timeout (float): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - tag (list[str,,]): รายการแท็กที่ต้องการค้นหา (default เป็น ['div', 'span', 'a', 'button'])
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าเจอ Tag ที่ต้องการจะคืนออกมาเป็น อ็อบเจ็กต์ selenium.webdriver.remote.webelement.WebElement
      - ถ้าไม่เจอ Tag จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.OO00OO000O00OOOO0 (driver , text , timeout, tag , mark , showdb )

  # --- ค้นหา Text แบบ contains หลายตำแหน่ง
  def find_text_contains_by_xpath_muti ( driver , text , timeout=0.5 , tag=['div','span','a','button']  , mark=True , showdb=False ):

    """
    ค้นหาข้อความบนหน้าเว็บด้วย XPath ในแท็กที่ระบุ ( ค้นหาแบบ contains ).

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - text (str): ข้อความที่ต้องการค้นหาในหน้าเว็บ
      - timeout (float): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - tag (list[str,,]): รายการแท็กที่ต้องการค้นหา (default เป็น ['div', 'span', 'a', 'button'])
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าเจอ Tag ที่ต้องการจะคืนออกมาเป็น อ็อบเจ็กต์รูปแบบ List [selenium.webdriver.remote.webelement.WebElement]
      - ถ้าไม่เจอ Tag จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.O0OO00000OOO0OO0O (driver , text , timeout, tag , mark , showdb )

  # --- ค้นหา attribute
  def find_attribute_by_xpath (driver ,attribute =[[]],tag =['div','span','a','button'],timeout =0.5 , mark=True , showdb=False ):

    """
    ค้นหาแท็กที่มี attribute ที่ระบุด้วย XPath ในแท็กที่ระบุ.

    พารามิเตอร์:
        - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
        - attribute (list[str,,]): รายการของ attribute ในแท็กที่ต้องการค้นหา (default เป็น [[]] )
        - tag (list[str,,]): รายการแท็กที่ต้องการค้นหา (default เป็น ['div', 'span', 'a', 'button'])
        - timeout (float, optional): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
        - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
        - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าเจอ Tag ที่ต้องการจะคืนออกมาเป็น อ็อบเจ็กต์ selenium.webdriver.remote.webelement.WebElement
      - ถ้าไม่เจอ Tag จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.O000OO0O00O0OO00O (driver ,attribute ,tag ,timeout , mark , showdb  )

  # --- ค้นหา attribute หลายตำแหน่ง
  def find_attribute_by_xpath_muti ( driver , attribute=[[]]  , tag=['div','span','a','button']  , timeout=0.5  , mark=True , showdb=False ):

    """
    ค้นหาแท็กที่มี attribute ที่ระบุด้วย XPath ในแท็กที่ระบุ.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - attribute (list[str,,]): รายการของ attribute ในแท็กที่ต้องการค้นหา (default เป็น [[]] )
      - tag (list[str,,]): รายการแท็กที่ต้องการค้นหา (default เป็น ['div', 'span', 'a', 'button'])
      - timeout (float, optional): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าเจอ Tag ที่ต้องการจะคืนออกมาเป็น อ็อบเจ็กต์รูปแบบ List [selenium.webdriver.remote.webelement.WebElement]
      - ถ้าไม่เจอ Tag จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.O0O0O000OOOOO0O00 (driver , attribute, tag  , timeout , mark , showdb )

  # --- ค้นหา attribute แบบ contains
  def find_attribute_contains_by_xpath ( driver , attribute=[[]]  , tag=['div','span','a','button']  , timeout=0.5 , mark=True , showdb=False  ) :

    """
    ค้นหาแท็กที่มี attribute ที่ระบุด้วย XPath ในแท็กที่ระบุ ( ค้นหาแบบ contains ).

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - attribute (list[str,,]): รายการของ attribute ในแท็กที่ต้องการค้นหา (default เป็น [[]] )
      - tag (list[str,,]): รายการแท็กที่ต้องการค้นหา (default เป็น ['div', 'span', 'a', 'button'])
      - timeout (float, optional): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าเจอ Tag ที่ต้องการจะคืนออกมาเป็น อ็อบเจ็กต์ selenium.webdriver.remote.webelement.WebElement
      - ถ้าไม่เจอ Tag จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.OO00OOO0000OO000O (driver , attribute, tag  , timeout , mark , showdb )

  # --- ค้นหา attribute แบบ contains หลายตำแหน่ง
  def find_attribute_contains_by_xpath_muti ( driver , attribute=[[]]  , tag=['div','span','a','button']  , timeout=0.5 , mark=True , showdb=False  ):

    """
    ค้นหาแท็กที่มี attribute ที่ระบุด้วย XPath ในแท็กที่ระบุ ( ค้นหาแบบ contains ).

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - attribute (list[str,,]): รายการของ attribute ในแท็กที่ต้องการค้นหา (default เป็น [[]] )
      - tag (list[str,,]): รายการแท็กที่ต้องการค้นหา (default เป็น ['div', 'span', 'a', 'button'])
      - timeout (float, optional): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าเจอ Tag ที่ต้องการจะคืนออกมาเป็น อ็อบเจ็กต์รูปแบบ List [selenium.webdriver.remote.webelement.WebElement]
      - ถ้าไม่เจอ Tag จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.O0OO0OOOO0OO0OO00 (driver , attribute, tag , timeout , mark , showdb )

  # --- ค้นหา Xpath แบบ Custom
  def find_custom_xpath ( driver , xpath ='' , timeout =0.5 , mark=True , showdb=False ):

    """
    ค้นหาองค์ประกอบบนหน้าเว็บด้วย XPath ที่กำหนดเอง.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - xpath (str): XPath ที่กำหนดเองที่ใช้ในการค้นหาองค์ประกอบบนหน้าเว็บ (default เป็น '')
      - timeout (float): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าเจอ Tag ที่ต้องการจะคืนออกมาเป็น อ็อบเจ็กต์ selenium.webdriver.remote.webelement.WebElement
      - ถ้าไม่เจอ Tag จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.O00O00O00OO0OO0OO (driver , xpath , timeout  , mark , showdb )

  # --- ค้นหา Xpath หลายตำแหน่ง แบบ Custom
  def find_custom_xpath_muti ( driver , xpath ='' , timeout =0.5 , mark=True , showdb=False ):

    """
    ค้นหาแท็กที่มี attribute ที่ระบุด้วย XPath ในแท็กที่ระบุ ( ค้นหาแบบ contains ).

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - xpath (str): XPath ที่กำหนดเองที่ใช้ในการค้นหาองค์ประกอบบนหน้าเว็บ (default เป็น '')
      - timeout (float): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าเจอ Tag ที่ต้องการจะคืนออกมาเป็น อ็อบเจ็กต์รูปแบบ List [selenium.webdriver.remote.webelement.WebElement]
      - ถ้าไม่เจอ Tag จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.OOOOO000O00000O00 (driver , xpath , timeout , mark , showdb  )

  # --- คลิก element
  def click_by_xpath ( driver , element_path , count=1 , delay=0.1 , mode=1 ,  showdb=False  ) :

    """
    คลิกองค์ประกอบของ Selenium โดยใช้ XPath ที่กำหนด.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - element_path (selenium.webdriver.remote.webelement.WebElement): อ็อบเจ็กต์ Element ของ Selenium ที่ต้องการคลิก
      - count (int): จำนวนครั้งที่ต้องการคลิก (default เป็น 1)
      - delay (float): เวลาที่รอระหว่างการคลิก (เป็นจำนวนวินาที, default เป็น 0.1)
      - mode (int): โหมดในการทำงาน (1-4) (default เป็น 1)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.OO00000OOO00OO0OO (driver , element_path , count, delay, mode , showdb)

  # --- คลิก แบบ Muti element
  def click_muti_by_xpath ( driver , element_path=[] , count=1 , delay=0.1 , mode=1 ,  showdb=False  ):

    """
    คลิกองค์ประกอบของ Selenium โดยใช้ XPath ที่กำหนด.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - element_path (List[selenium.webdriver.remote.webelement.WebElement]): อ็อบเจ็กต์ Element ของ Selenium ที่ต้องการคลิก
      - count (int): จำนวนครั้งที่ต้องการคลิก (default เป็น 1)
      - delay (float): เวลาที่รอระหว่างการคลิก (เป็นจำนวนวินาที, default เป็น 0.1)
      - mode (int): โหมดในการทำงาน (1-4) (default เป็น 1)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคืนค่า False
    """
    
    return O0OOO0O0O0OO00OOO.O00O0OOOO0OOO00OO (driver , element_path, count, delay, mode , showdb)

  # --- เคลีย input
  def clear_input_by_xpath ( driver , element_path , mode=1 ,  showdb=False ):

    """
    เคลียร์ข้อมูล input ขององค์ประกอบโดยใช้ XPath ที่กำหนด.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - element_path (selenium.webdriver.remote.webelement.WebElement): อ็อบเจ็กต์ Element ของ Selenium ที่ต้องการเคลียร์ข้อมูล input
      - mode (int): โหมดในการทำงาน (1-3) (default เป็น 1)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้า Error จะคืนค่า False
    """
    return O0OOO0O0O0OO00OOO.OO00OOO000O0O0OOO (driver , element_path , mode , showdb)
  
  # --- พิมข้อความ input
  def insert_input_by_xpath ( driver  , text , element_path , mode=1 , showdb=False ):

    """
    พิมพ์ข้อความลงใน input โดยใช้ XPath ที่กำหนด.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - text (str): ข้อความที่ต้องการพิมลงใน input
      - element_path (selenium.webdriver.remote.webelement.WebElement): อ็อบเจ็กต์ Element ของ Selenium ที่ต้องการพิมข้อความ
      - mode (int, optional): โหมดในการทำงาน (1-3) (default เป็น 1)
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้า Error จะคืนค่า False
    """
    return O0OOO0O0O0OO00OOO.O00OOOOOO0O0O0O0O (driver  , text , element_path , mode , showdb)

  # --- เลื่อน Scroll ตาม Tag 
  def scroll_to_element_by_xpath( driver , element_path , mode=1 , showdb=False ) :

    """
    เลื่อน scroll ไปยังองค์ประกอบที่กำหนดโดย XPath.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - element_path (selenium.webdriver.remote.webelement.WebElement): อ็อบเจ็กต์ Element ของ Selenium ที่ต้องการเลื่อน scroll ให้มองเห็น
      - mode (int, optional): โหมดในการทำงาน (1-2) (default เป็น 1)
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.OO0O0O00OOO000OO0(driver , element_path , mode , showdb)

  # --- เลื่อน Target ตาม Tag
  def move_to_element_by_xpath( driver , element_path  , showdb=False ) :

    """
    เลื่อน หน้าจอ ไปยังองค์ประกอบที่กำหนดโดย XPath.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - element_path (selenium.webdriver.remote.webelement.WebElement): อ็อบเจ็กต์ Element ของ Selenium ที่ต้องการเลื่อนเมาส์ไปยัง
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.O00000OO0O0O0O0OO( driver , element_path , showdb )
  
  # --- เลื่อน Target ตาม Tag แบบ หลายๆ Tag
  def move_to_element_list_by_xpath( driver , element_list ,  showdb=False ) :

    """
    เลื่อน หน้าจอ ไปยังองค์ประกอบที่กำหนดโดย XPath ( เลื่อนหน้าจอแบบหลาย element พร้อมกัน ).

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - element_list (List[selenium.webdriver.remote.webelement.WebElement]): ลิสต์ของอ็อบเจ็กต์ Element ของ Selenium ที่ต้องการเลื่อนเมาส์ไปยัง
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.OO0O0000OOO000OO0( driver , element_list  , showdb)

  # --- Drop ภาพลง element
  def drop_file_by_xpath( driver , element_path , path_file , mode=1, showdb=False  ):

    """
    Drop ไฟล์ลงในองค์ประกอบโดย XPath.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - element_path (selenium.webdriver.remote.webelement.WebElement): อ็อบเจ็กต์ Element ของ Selenium ที่ต้องการวางไฟล์ลงไป
      - path_file (str): ตำแหน่งที่เก็บไฟล์ที่ต้องการ Drop ไฟล์
      - mode (int, optional): โหมดในการทำงาน (1-3) (default เป็น 1)
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.O000000OOOO00O0O0(driver , element_path , path_file , mode , showdb)

  # --- ลากและวาง Element
  def drag_and_drop_by_xpath( driver , element_first , element_last ,  showdb=False  ):

    """
    ลากและวาง Element โดยใช้ XPath.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - element_first (selenium.webdriver.remote.webelement.WebElement): อ็อบเจ็กต์ Element ของ Selenium ที่ต้องการลาก
      - element_last (selenium.webdriver.remote.webelement.WebElement): อ็อบเจ็กต์ Element ของ Selenium ที่ต้องการวาง
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคืนค่า False
    """
    return O0OOO0O0O0OO00OOO.O0OOO000O0O0OO0OO( driver , element_first , element_last   , showdb)
  
  # --- เลื่อน Scroll ทั้งหน้า
  def scroll_max( driver ,  showdb=False ) :

    """
    เลื่อน Scroll ทั้งหน้า.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคืนค่า False
    """
    return O0OOO0O0O0OO00OOO.OO0O0000OO0O0OO00( driver , showdb )
  
  # --- เลื่อน Scroll กำหนด % ความสูง
  def scroll_custom( driver , target , showdb=False ) :

    """
    เลื่อน Scroll โดยกำหนดเปอร์เซ็นต์ของการเลื่อนสกอร์บาร์ (ระหว่าง 1 - 100).

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - target (int): เปอร์เซ็นต์ของการเลื่อนสกอร์บาร์ที่ต้องการ (ระหว่าง 1 - 100)
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าทำงานถูกต้องจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.OOO00000O00OOO000( driver , target  , showdb)
        
  # == จับเวลา
  def time_out( min , sec ,  showdb=False ):

    """
    จับเวลาด้วยหน่วยนาทีและวินาที.

    พารามิเตอร์:
      - min (int): หน่วยนาทีที่ต้องการจับเวลา
      - sec (int): หน่วยวินาทีที่ต้องการจับเวลา
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้าถึงเวลาที่กำหนดจะคืนค่าออกมาเป็น True
      - ถ้า Error จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.O0O0000OOO00000OO( min , sec   , showdb)
  
  # == คลิก alert box
  def alert_box (driver ,  showdb=False ):

    """
    คลิก alert box.

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - showdb (bool, optional): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)

    ผลลัพธ์:
      - ถ้า Error จะคืนค่า False
    """

    return O0OOO0O0O0OO00OOO.OO000O000O0OO0OO0(driver , showdb)

class captcha_solver :

  # == แก้ แคปช่า Tiktok แบบวงล้อ
  def tiktok_captcha_whirl( driver , timeout=0.2 , mark=False , showdb=False , token="" ) :

    """
    แก้ แคปช่า Tiktok แบบวงล้อ.
    ความแม่นยำ 90 - 95%

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - timeout (float): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)
      - token (str): token ของ TikTok Captcha Solver

    ผลลัพธ์:
      - ถ้า Error จะคืนค่า False
    """

    return OO0O0OOO0000O00O0.O00000OO0O0O0O0OO (driver ,timeout,mark,showdb,token)

  # == แก้ แคปช่า Tiktok แบบพิชซ่า
  def tiktok_captcha_puzzle( driver , timeout=0.2 , mark=False , showdb=False  , token=''  ) :

    """
    แก้ แคปช่า Tiktok แบบพิชซ่า.
    ความแม่นยำ 90 - 95%

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - timeout (float): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)
      - token (str): token ของ TikTok Captcha Solver

    ผลลัพธ์:
      - ถ้า Error จะคืนค่า False
    """

    return OO0O0OOO0000O00O0.OOO00000O00OOO000 (driver ,timeout,mark,showdb,token)

  # == แก้ แคปช่า Tiktok แบบ 3D
  def tiktok_captcha_3d( driver , timeout=0.2 , mark=False , showdb=False  , token=''  ) :

    """
    แก้ แคปช่า Tiktok แบบ 3D.
    ความแม่นยำ 60 - 65%

    พารามิเตอร์:
      - driver (selenium.webdriver): อ็อบเจ็กต์ของ Selenium WebDriver ที่ใช้ในการควบคุมเบราว์เซอร์
      - timeout (float): เวลาที่รอให้โหลดแท็กหลังจากค้นหา (เป็นจำนวนวินาที, default เป็น 0.5)
      - mark (bool): กำหนดให้เป็น True เพื่อตีกรอบสีแดงใน Tag HTML หรือเป็น False หากไม่ต้องการ (default เป็น True)
      - showdb (bool): กำหนดให้เป็น True เพื่อแสดงการทำงานของโค้ดหรือเป็น False หากไม่ต้องการ (default เป็น False)
      - token (str): token ของ TikTok Captcha Solver

    ผลลัพธ์:
      - ถ้า Error จะคืนค่า False
    """

    return OO0O0OOO0000O00O0.OOOO0OOOOOOO000OO (driver ,timeout,mark,showdb,token)

