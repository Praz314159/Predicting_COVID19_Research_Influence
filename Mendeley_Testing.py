'''
Testing the Mendely API 
'''
#importing Mendeley
from mendeley import Mendeley 

session_secret = 'oFuZqBUHDmKZpIYC'
redirect_url = 'http://localhost:5000/oauth'
client_id = 9185 

mendeley_session = Mendeley(client_id, session_secret)
working_session = mendeley_session.start_client_credentials_flow().authenticate() 
#auth = mendeley_session.start_authorization_code_flow() 
#working_session = auth.authenticate(auth_response)

doc = working_session.catalog.by_identifier(doi='10.1371/journal.pmed.0020124', view='stats') 
:









print("PAPER TITLE: ", doc.title)
print("READER STATS BY ACADEMIC RANK: ", doc.reader_count_by_academic_status)

