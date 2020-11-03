from PyQt5 import QtGui
from PyQt5.QtGui import QImage,QPixmap
from  PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget,QMainWindow
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import (QThread, Qt, pyqtSignal)
from maintest import Gui_Controller, PlotCanvas
import plots
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from searchModel import Recherche_modelBooleen,Recherche_ModelVectoriel,evaluerModelVectoriel
import operator,nltk

class EvalThread(QThread):
    changePixmap = pyqtSignal(QImage)
    
    def __init__(self,controller:Gui_Controller,methode,flag=1,fixedDocnumber=50):
        super().__init__()
        self.controller=controller
        self.methode=methode
        self.FLAG=flag
        self.docnumber=fixedDocnumber

    

    def run(self):
        
        

        if self.FLAG==1:
        
            requests=list(self.controller.requests.values())
            moysRappels=nltk.defaultdict(float)
            moysPrecision=nltk.defaultdict(float)
            for request in requests:
                
                self.controller.gui.requestContentLabel.setText(request)
                
                modelResults=Recherche_ModelVectoriel(None,request,self.methode,self.controller.seuil_rsv)
                
                modelResults=sorted(modelResults.items(), key=operator.itemgetter(1),reverse=True)
                finalresults=[el[0] for el in  modelResults if el[1]>self.controller.seuil_rsv]
                if len(finalresults)==0:
                    finalresults=[el[0] for el in  modelResults if el[1]>0.0]
                
                for i in range(1,50):
                    result=evaluerModelVectoriel(finalresults[:i],requests.index(request),self.methode)
                    self.controller.allResults[request].append((result[0],result[1],i))
                    moysRappels[i]+=result[0]/len(requests)
                    moysPrecision[i]+=result[1]/len(requests)

                
                best=max(self.controller.allResults[request])
                print("Meilleur résultats pour : \n \t << ",request," >> \n \t ",best)

            try:
                points=[(moysRappels[i],moysPrecision[i]) for i in range(1,len(requests))]  

                points=sorted(points,key=lambda tuple:tuple[0])
                self.controller.results=points
                self.controller.gui.plotButton.click()
                print("finished") 
            except Exception as e:
                print("Error occured when trying to plot results \n \t"+str(e))  


        elif self.FLAG==2:
            requests=list(self.controller.requests.values())
            moysRappels=nltk.defaultdict(float)
            moysPrecision=nltk.defaultdict(float)
            for request in requests:
                
                self.controller.gui.requestContentLabel.setText(request)
                
                modelResults=Recherche_ModelVectoriel(None,request,self.methode,self.controller.seuil_rsv)
                
                modelResults=sorted(modelResults.items(), key=operator.itemgetter(1),reverse=True)
                finalresults=[el[0] for el in  modelResults if el[1]>self.controller.seuil_rsv]
                if len(finalresults)==0:
                    finalresults=[el[0] for el in  modelResults if el[1]>0.0]
                
                for seuil in range(0.0,0.5,0.05):
                    result=evaluerModelVectoriel(finalresults[:self.docnumber],requests.index(request),self.methode)
                    self.controller.allResults[request].append((result[0],result[1],seuil))
                    moysRappels[i]+=result[0]/len(requests)
                    moysPrecision[i]+=result[1]/len(requests)

                
                best=max(self.controller.allResults[request])
                print("Meilleur résultats pour : \n \t << ",request," >> \n \t ",best)

            try:
                points=[(moysRappels[i],moysPrecision[i]) for i in range(1,len(requests))]  

                points=sorted(points,key=lambda tuple:tuple[0])
                self.controller.results=points
                self.controller.gui.plotButton.click()
                print("finished") 
            except Exception as e:
                print("Error occured when trying to plot results \n \t"+str(e))                      

            
            
