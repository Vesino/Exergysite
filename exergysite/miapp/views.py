from django.shortcuts import render_to_response
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from pvlib import irradiance, atmosphere, pvsystem
from pvlib.location import Location
from pvlib.forecast import GFS, NAM
from pvlib.pvsystem import retrieve_sam
from pvlib.tracking import SingleAxisTracker
from pvlib.modelchain import ModelChain


# Create your views here.
def index(request):
    return render_to_response('miapp/index.html')
