import os.path
import subprocess
import glob


USB_DRIVE = 'E:/'

TV32_315_INI_FILE = 'panatv-PT320AT01-ref53-full.ini'
TV32_315_INI_FILE_PANA = 'panatv-PT320AT01-ref53-full.ini'
TV32_320_INI_FILE = 'panatv-PT320AT01-ref53-full.ini'
TV32_JP_INI_FILE = 'allupgrade_msd338_4G_1G_ref30.ini'
TV40_INI_FILE = 'panatv-PT320AT01-ref59-full.ini'
TV40_HL_INI_FILE_PANA = 'allupgrade_msd338_4G_ref68.ini'
TV50_INI_FILE = 'allupgrade_msd338_8G_1G_ref60.ini'
TV50_INI_FILE_PANA = 'allupgrade_msd338_8G_1G_ref60.ini'
TV50_SQ5_INI_FILE_PANA = 'allupgrade_msd338_8G_1G_ref60.ini'
TV55_INI_FILE = 'allupgrade_msd338_8G_1G_ref60.ini'
TV55_INI_FILE_PANA = 'allupgrade_msd338_8G_1G_ref60.ini'
##########################################################
MSTAR_32_315 = './../mstar-bin-tool-32-315-v2/'
MSTAR_32_315_PANA = './../mstar-bin-tool-32-315-v2-pana/'
MSTAR_32_320 = './../mstar-bin-tool-32-320-v2/'
MSTAR_32_JP = './../mstar-bin-tool-32-JP/'
MSTAR_40 = './../mstar-bin-tool-40-v3/'
MSTAR_40_HL_PANA = './../mstar-bin-tool-40-v3-HL-pana/'
MSTAR_50 = './../mstar-bin-tool-50-v3/'
MSTAR_50_PANA = './../mstar-bin-tool-50-v3-pana/'
MSTAR_50_SQ5 = './../mstar-bin-tool-50-v3-sq5/'
MSTAR_50_SQ5_PANA = './../mstar-bin-tool-50-v3-sq5-pana/'
MSTAR_55 = './../mstar-bin-tool-55-v3/'
MSTAR_55_PANA = './../mstar-bin-tool-55-v3-pana/'
##########################################################
MSTAR_32_315_BIN = 'allupgrade_msd338_4G_ref54.bin'
MSTAR_32_315_BIN_PANA = 'allupgrade_msd338_4G_ref54.bin'
MSTAR_32_320_BIN = 'allupgrade_msd338_4G_ref54.bin'
MSTAR_32_JP_BIN = 'allupgrade_msd338_4G_1G_ref30.bin'
MSTAR_40_BIN = 'allupgrade_msd338_4G_1G_ref59.bin'
MSTAR_40_BIN_HL_PANA = 'allupgrade_msd338_4G_ref68.bin'
MSTAR_50_BIN = 'allupgrade_msd338_8G_1G_ref60.bin'
MSTAR_50_BIN_PANA = 'allupgrade_msd338_8G_1G_ref60.bin'
MSTAR_50_SQ5_BIN = 'allupgrade_msd338_8G_1G_ref60.bin'
MSTAR_50_SQ5_BIN_PANA = 'allupgrade_msd338_8G_1G_ref60.bin'

MSTAR_55_BIN = 'allupgrade_msd338_8G_1G_ref60.bin'
MSTAR_55_BIN_PANA = 'allupgrade_msd338_8G_1G_ref60.bin'
##########################################################
MSTAR_32_Android = 'MSTAR_32_Android/'
MSTAR_32_Android_PANA = 'MSTAR_32_Android/'
MSTAR_40_Android = 'MSTAR_40_Android/'
MSTAR_40_Android_HL_PANA = 'MSTAR_40_Android/'

MSTAR_50_Android = 'MSTAR_50_Android/'
MSTAR_50_Android_PANA = 'MSTAR_50_Android/'
MSTAR_50_SQ5_Android = 'MSTAR_50_Android/'
MSTAR_50_SQ5_Android_PANA = 'MSTAR_50_Android/'


MSTAR_55_Android = 'MSTAR_55_Android/'
MSTAR_55_Android_PANA = 'MSTAR_55_Android/'

USER_SYSTEM_APKS = 'temp/system/media/user_system_apks/'
NEW_USER_APKS = './../new_apks/'
CONFIGS = 'configs/'
PANA_PACK = 'pana_pack/'
NEW_SYSTEM_IMAGE_FILE = 'new_system.img'
SYSTEM_IMAGE_FILE = 'system.img'

	
def add_hex_value_by_1(hex_str):
	hex_int = int(hex_str, 16)
	new_int = hex_int + 1
	if 'L' in hex(new_int):
		return hex(new_int)[:-1]
	else:	
		return hex(new_int)
def modify_CRC(cwd, ini_file):
	file_name = cwd + 'configs/' + ini_file
	print file_name
	#file_name = file_name.replace('/', '\\')
	temp_file_name =  cwd + 'configs/temp.ini'
	fread = open(file_name, 'r')
	fwrite = open(temp_file_name, 'w')
	line_num = 0
	# search for lines that contain 'CEnv_UpgradeCRC_Tmp' and 'CEnv_UpgradeCRC_Val'
	# get the CRC number and add it by 1
	for line in fread:
		if 'setenv CEnv_UpgradeCRC_Tmp' in line:
			print str(line_num) + ': ' + line
			list_word = line.split()
			list_word[2] = add_hex_value_by_1(list_word[2])
			line = '\t' + list_word[0] + ' ' + list_word[1] + ' ' + list_word[2] + '\n'
			fwrite.write(line)
		elif 'setenv CEnv_UpgradeCRC_Val' in line:
			print str(line_num) + ': ' + line
			list_word = line.split()
			list_word[2] = add_hex_value_by_1(list_word[2])
			line = '\t' + list_word[0] + ' ' + list_word[1] + ' ' + list_word[2] + '\n'
			fwrite.write(line)
		else:
			fwrite.write(line)
	fread.close()
	fwrite.close()
	
	#remove the old file, and rename the temp file
	remove_command = 'rm ' + file_name
	rename_command = 'ren ' + temp_file_name + ' ' + ini_file
	rename_command = rename_command.replace('/', '\\')
	print remove_command
	print rename_command
	subprocess.call(remove_command, shell=True)
	subprocess.call(rename_command, shell=True)
	

	

def copy_system_image(cwd, mstar_android):
	copy_new_image = 'cp ' + mstar_android + NEW_SYSTEM_IMAGE_FILE + ' ' + cwd + PANA_PACK
	remove_old_image = 'rm ' + cwd +  PANA_PACK  + SYSTEM_IMAGE_FILE 
	rename_new_image  = 'ren ' + cwd + PANA_PACK  + NEW_SYSTEM_IMAGE_FILE + ' ' + SYSTEM_IMAGE_FILE
	# copy_new_image = copy_new_image.replace('/', '/');
	# remove_old_image = remove_old_image.replace('/', '/');
	rename_new_image = rename_new_image.replace('/', '\\')
	print cwd + mstar_android + NEW_SYSTEM_IMAGE_FILE + '\n'
	if(os.path.isfile(cwd + mstar_android + NEW_SYSTEM_IMAGE_FILE)):
		print copy_new_image
		process = subprocess.call(copy_new_image, shell=True)
		if(os.path.isfile( cwd + PANA_PACK + SYSTEM_IMAGE_FILE)):
			print remove_old_image
			subprocess.call(remove_old_image, shell=True) 
		subprocess.call(rename_new_image, shell=True)
		print rename_new_image

def delete_user_apks(user_system_apks):
	list_apks = glob.glob(user_system_apks + '*.apk')
	print list_apks
	for apk in list_apks:
		apk = apk.replace('\\', '/')
		delete_apk = 'rm ' + apk
		print delete_apk
		subprocess.call(delete_apk, shell=True)
		
def copy_apks(user_system_apks):
	list_apks = glob.glob(NEW_USER_APKS + '*.apk')
	print list_apks
	for apk in list_apks:
		apk = apk.replace('\\', '/')
		user_system_apks = user_system_apks.replace('\\', '/')
		copy_apk = 'cp ' + apk + ' ' + user_system_apks
		print copy_apk
		subprocess.call(copy_apk, shell=True)

def build_bin_file(ini_file, cwd):
	command = 'python pack.py ' + 'configs/' + ini_file
	process = subprocess.Popen(command, cwd = cwd, stdout=subprocess.PIPE)
	output, err = process.communicate()
	print output
	print('=================================================================')
	print('                            COMPLETED                            ')
	print('=================================================================')
	#subprocess.call('python pack.py ' + 'configs/' + ini_file, cwd = cwd, shell=True) 
	#pass
def build_system_file(cwd):
	subprocess.call('START /WAIT ' + cwd + 'START.exe', shell=True)


def copy_bin_file_to_thumb_drive(mstar_bin_file, mstar_folder):
	bin_file = USB_DRIVE + mstar_bin_file
	if(os.path.exists(bin_file)):
		remove_command = 'rm ' + bin_file
		subprocess.call(remove_command, shell = True)
	print('=================================================================')
	print('                            Copying bin file                     ')
	print('=================================================================')
	copy_command = 'cp ' + mstar_folder + mstar_bin_file + ' ' + USB_DRIVE
	subprocess.call(copy_command, shell=True)
	print('=================================================================')
	print('                            Done                                 ')
	print('=================================================================')
	pass	

def build_rom_procedure(cwd, mstar_android, ini_file):
	pass	
	
def TV_32_Panel_315_copy():
	copy_bin_file_to_thumb_drive(MSTAR_32_315_BIN, MSTAR_32_315)

def TV_32_Panel_315():
	if os.path.exists(MSTAR_32_315):
		cwd = MSTAR_32_315
		mstar_android = cwd + MSTAR_32_Android
		ini_file = TV32_315_INI_FILE
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('----------------------------------------------------------------------')
		print('----------------------- Copying new apks -----------------------------')
		print('----------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('----------------------------------------------------------------------')
		print('----= ---------------- Building a system image -----------------------')
		print('----------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('----------------------------------------------------------------------')
		print('--------------------- Copying a system image -------------------------')
		print('----------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('----------------------------------------------------------------------')
		print ('---------------------- Modifying CRC --------------------------------')
		print('----------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('----------------------------------------------------------------------')
		print('--------------------- Building bin file ------------------------------')
		print('----------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_32_Panel_315')
		
#################################################################################
#################################################################################
def TV_32_Panel_315_copy_pana():
	copy_bin_file_to_thumb_drive(MSTAR_32_315_BIN_PANA, MSTAR_32_315_PANA)

def TV_32_Panel_315_pana():
	if os.path.exists(MSTAR_32_315_PANA):
		cwd = MSTAR_32_315_PANA
		mstar_android = cwd + MSTAR_32_Android_PANA
		ini_file = TV32_315_INI_FILE_PANA
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('----------------------------------------------------------------------')
		print('----------------------- Copying new apks -----------------------------')
		print('----------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('----------------------------------------------------------------------')
		print('----= ---------------- Building a system image -----------------------')
		print('----------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('----------------------------------------------------------------------')
		print('--------------------- Copying a system image -------------------------')
		print('----------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('----------------------------------------------------------------------')
		print ('---------------------- Modifying CRC --------------------------------')
		print('----------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('----------------------------------------------------------------------')
		print('--------------------- Building bin file ------------------------------')
		print('----------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_32_Panel_315_PANA')
		
#################################################################################
#################################################################################
def TV_32_Panel_320_copy():
	copy_bin_file_to_thumb_drive(MSTAR_32_320_BIN, MSTAR_32_320)
	pass

def TV_32_Panel_320():
	if os.path.exists(MSTAR_32_320):
		cwd = MSTAR_32_320
		mstar_android = cwd + MSTAR_32_Android
		ini_file = TV32_320_INI_FILE
	
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('-------------------------------------------------------------------')
		print('----------------------- Copying new apks --------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('--------------------------------------------------------------------')
		print('----= ---------------- Building system image -----------------------')
		print('--------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('-------------------------------------------------------------------')
		print('--------------------- Copying system image ------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('-------------------------------------------------------------------')
		print ('---------------------- Modifying CRC -----------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('-------------------------------------------------------------------')
		print('--------------------- Building bin file ---------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_32_Panel_320')

#################################################################################
#################################################################################
def TV_32_JP_copy():
	copy_bin_file_to_thumb_drive(MSTAR_32_JP_BIN, MSTAR_32_JP)
	pass

def TV_32_JP():
	if os.path.exists(MSTAR_32_JP):
		cwd = MSTAR_32_JP
		mstar_android = cwd + MSTAR_32_Android
		ini_file = TV32_JP_INI_FILE
	
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('-------------------------------------------------------------------')
		print('----------------------- Copying new apks --------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('--------------------------------------------------------------------')
		print('----= ---------------- Building system image -----------------------')
		print('--------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('-------------------------------------------------------------------')
		print('--------------------- Copying system image ------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('-------------------------------------------------------------------')
		print ('---------------------- Modifying CRC -----------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('-------------------------------------------------------------------')
		print('--------------------- Building bin file ---------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_32_JP')

#################################################################################
#################################################################################		
def TV_40_JP_copy():
	copy_bin_file_to_thumb_drive(MSTAR_40_BIN, MSTAR_40)
	pass

def TV_40_JP():
	if os.path.exists(MSTAR_40):
		cwd = MSTAR_40
		mstar_android = cwd + MSTAR_40_Android
		ini_file = TV40_INI_FILE
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('-------------------------------------------------------------------')
		print('----------------------- Copying new apks --------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('--------------------------------------------------------------------')
		print('----= ---------------- Building a system image ---------------------')
		print('--------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('-------------------------------------------------------------------')
		print('--------------------- Copying a system image ----------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('-------------------------------------------------------------------')
		print ('---------------------- Modify CRC --------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('-------------------------------------------------------------------')
		print('--------------------- Build bin file ------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_40')


#################################################################################
#################################################################################		
def TV_40_HL_copy_pana():
	copy_bin_file_to_thumb_drive(MSTAR_40_BIN_HL_PANA, MSTAR_40_HL_PANA)
	pass

def TV_40_HL_pana():
	if os.path.exists(MSTAR_40_HL_PANA):
		cwd = MSTAR_40_HL_PANA
		mstar_android = cwd + MSTAR_40_Android_HL_PANA
		ini_file = TV40_HL_INI_FILE_PANA
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('-------------------------------------------------------------------')
		print('----------------------- Copying new apks --------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('--------------------------------------------------------------------')
		print('----= ---------------- Building a system image ---------------------')
		print('--------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('-------------------------------------------------------------------')
		print('--------------------- Copying a system image ----------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('-------------------------------------------------------------------')
		print ('---------------------- Modify CRC --------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('-------------------------------------------------------------------')
		print('--------------------- Build bin file ------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_40 HL PANA')

#################################################################################
#################################################################################		
def TV_50_JP_copy():
	copy_bin_file_to_thumb_drive(MSTAR_50_BIN, MSTAR_50)
	pass

def TV_50_JP():
	if os.path.exists(MSTAR_50):
		cwd = MSTAR_50
		mstar_android = cwd + MSTAR_50_Android
		ini_file = TV50_INI_FILE
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('-------------------------------------------------------------------')
		print('----------------------- Copying new apks --------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('--------------------------------------------------------------------')
		print('----= ---------------- Building a system image ---------------------')
		print('--------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('-------------------------------------------------------------------')
		print('--------------------- Copying a system image ----------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('-------------------------------------------------------------------')
		print ('---------------------- Modify CRC --------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('-------------------------------------------------------------------')
		print('--------------------- Build bin file ------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_50')
#################################################################################
#################################################################################		
def TV_50_JP_copy_pana():
	copy_bin_file_to_thumb_drive(MSTAR_50_BIN_PANA, MSTAR_50_PANA)
	pass

def TV_50_JP_pana():
	if os.path.exists(MSTAR_50_PANA):
		cwd = MSTAR_50_PANA
		mstar_android = cwd + MSTAR_50_Android_PANA
		ini_file = TV50_INI_FILE_PANA
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('-------------------------------------------------------------------')
		print('----------------------- Copying new apks --------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('--------------------------------------------------------------------')
		print('----= ---------------- Building a system image ---------------------')
		print('--------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('-------------------------------------------------------------------')
		print('--------------------- Copying a system image ----------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('-------------------------------------------------------------------')
		print ('---------------------- Modify CRC --------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('-------------------------------------------------------------------')
		print('--------------------- Build bin file ------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_50')

#################################################################################
#################################################################################		
def TV_50_JP_SQ5_copy():
	copy_bin_file_to_thumb_drive(MSTAR_50_SQ5_BIN, MSTAR_50_SQ5)
	pass
def TV_50_JP_SQ5():
	if os.path.exists(MSTAR_50_SQ5):
		cwd = MSTAR_50_SQ5
		mstar_android = cwd + MSTAR_50_SQ5_Android
		ini_file = TV50_SQ5_INI_FILE
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('-------------------------------------------------------------------')
		print('----------------------- Copying new apks --------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('--------------------------------------------------------------------')
		print('----= ---------------- Building a system image ---------------------')
		print('--------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('-------------------------------------------------------------------')
		print('--------------------- Copying a system image ----------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('-------------------------------------------------------------------')
		print ('---------------------- Modify CRC --------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('-------------------------------------------------------------------')
		print('--------------------- Build bin file ------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_50_jp_SQ5')

#################################################################################
#################################################################################		
def TV_50_JP_SQ5_copy_pana():
	copy_bin_file_to_thumb_drive(MSTAR_50_SQ5_BIN_PANA, MSTAR_50_SQ5_PANA)
	pass
def TV_50_JP_SQ5():
	if os.path.exists(MSTAR_50_SQ5_PANA):
		cwd = MSTAR_50_SQ5_PANA
		mstar_android = cwd + MSTAR_50_SQ5_Android_PANA
		ini_file = TV50_SQ5_INI_FILE_PANA
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('-------------------------------------------------------------------')
		print('----------------------- Copying new apks --------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('--------------------------------------------------------------------')
		print('----= ---------------- Building a system image ---------------------')
		print('--------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('-------------------------------------------------------------------')
		print('--------------------- Copying a system image ----------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('-------------------------------------------------------------------')
		print ('---------------------- Modify CRC --------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('-------------------------------------------------------------------')
		print('--------------------- Build bin file ------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_50_jp_SQ5 PANA')
#################################################################################
#################################################################################		
def TV_55_HL_copy():
	copy_bin_file_to_thumb_drive(MSTAR_55_BIN, MSTAR_55)
	pass

def TV_55_HL():
	if os.path.exists(MSTAR_55):
		cwd = MSTAR_55
		mstar_android = cwd + MSTAR_55_Android
		ini_file = TV55_INI_FILE
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('-------------------------------------------------------------------')
		print('----------------------- Copying new apks --------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('--------------------------------------------------------------------')
		print('----= ---------------- Building a system image ---------------------')
		print('--------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('-------------------------------------------------------------------')
		print('--------------------- Copying a system image ----------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('-------------------------------------------------------------------')
		print ('---------------------- Modify CRC --------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('-------------------------------------------------------------------')
		print('--------------------- Build bin file ------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_55')

#################################################################################
#################################################################################		
def TV_55_HL_copy_pana():
	copy_bin_file_to_thumb_drive(MSTAR_55_BIN_PANA, MSTAR_55_PANA)
	pass

def TV_55_HL_pana():
	if os.path.exists(MSTAR_55_PANA):
		cwd = MSTAR_55_PANA
		mstar_android = cwd + MSTAR_55_Android_PANA
		ini_file = TV55_INI_FILE_PANA
	
		delete_user_apks(mstar_android + USER_SYSTEM_APKS)
		print('\n')
		print('-------------------------------------------------------------------')
		print('----------------------- Copying new apks --------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_apks(mstar_android + USER_SYSTEM_APKS)
		print('--------------------------------------------------------------------')
		print('----= ---------------- Building a system image ---------------------')
		print('--------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_system_file(mstar_android)
		print('-------------------------------------------------------------------')
		print('--------------------- Copying a system image ----------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		copy_system_image(cwd, mstar_android)
		print('-------------------------------------------------------------------')
		print ('---------------------- Modify CRC --------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		modify_CRC(cwd, ini_file)
		print('-------------------------------------------------------------------')
		print('--------------------- Build bin file ------------------------------')
		print('-------------------------------------------------------------------')
		print('\n')
		print('\n')
		build_bin_file(ini_file, cwd)
	else:
		print ('click_for_TV_55_PANA')
def test_import():
	print('build bin file scripts imported')