#start app
from fastapi import FastAPI
app = FastAPI()

#import versions here
from v1 import views
