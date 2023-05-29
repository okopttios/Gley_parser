import pygsheets


def update_gsh_azimyth(data):
    path = '/Users/andreykorniat/Documents/Project_DS/Gley_parser/lithe-center-369315-0f251401b4a4.json'
    gc = pygsheets.authorize(service_account_file=path)
    sh = gc.open('Parser_Gley') # Open the google sheet phthontest
    wks = sh[1] # select the first sheet 
    wks.clear()
    #wks.update_values('A2', data)
    wks.set_dataframe(data, (1,1),copy_index=False, copy_head=True, 
	    extend=False, fit=False)
    
def update_gsh_texnoto4ka(data):
    path = '/Users/andreykorniat/Documents/Project_DS/Gley_parser/lithe-center-369315-0f251401b4a4.json'
    gc = pygsheets.authorize(service_account_file=path)
    sh = gc.open('Parser_Gley') # Open the google sheet phthontest
    wks = sh[2] # select the first sheet 
    wks.clear()
    #wks.update_values('A2', data)
    wks.set_dataframe(data, (1,1),copy_index=False, copy_head=True, 
	    extend=False, fit=False)