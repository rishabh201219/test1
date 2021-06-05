import pickle
from flask import Flask, request, jsonify,render_template

from model_files.ml_model import predict_mpg
app = Flask(__name__)




model = pickle.load(open('model.pkl', 'rb')) 

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/form")
def form():
    return render_template('form.html')



@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method =='POST': 
      Cylinders = request.form['Cylinders']
      Cylinders= int(Cylinders)

      Cylinder = request.form['Cylinder']
      Cylinder = int(Cylinder)

      Cylinde = request.form['Cylinde']
      Cylinde = int(Cylinde)

      Displacement =request.form['Displacement']
      Displacement = int(Displacement)

      Displacemen = request.form['Displacemen']
      Displacemen = int(Displacemen)

      Displaceme = request.form['Displaceme']
      Displaceme = int(Displaceme)

      Horsepower =request.form['Horsepower']
      Horsepower = int(Horsepower)

      Horsepowe =request.form['Horsepowe']
      Horsepowe = int(Horsepowe)

      Horsepow = request.form['Horsepow']
      Horsepow = int(Horsepow)

      Weight = request.form['Weight']
      Weight = int(Weight)

      Weigh = request.form['Weigh']
      Weigh = int(Weigh)

      Weig = request.form['Weig']
      Weig = int(Weig)

      Acceleration =request.form['Acceleration']
      Acceleration = int(Acceleration)

      Acceleratio = request.form['Acceleratio']
      Acceleratio = int(Acceleratio)

      Accelerati =request.form['Accelerati']
      Accelerati = int(Accelerati)

      Model_Year = request.form['Model Year']
      Model_Year = int(Model_Year)

      Model_Yea = request.form['Model Yea']
      Model_Yea = int(Model_Yea)

      Model_Ye = request.form['Model Ye']
      Model_Ye = int(Model_Ye)
      
      Origin =request.form['Origin']
      Origin = int(Origin)
      
      Origi = request.form['Origi']
      Origi = int(Origi)
      
      Orig = request.form['Orig']
      Orig = int(Orig)
      vehicle_config = [[Cylinders, Cylinder, Cylinde], [Displacement, Displacemen, Displaceme], [
          Horsepower, Horsepowe, Horsepow], [Weight, Weigh, Weig], [Acceleration, Acceleratio, Accelerati], [Model_Year, Model_Yea, Model_Ye], [Origin, Origi, Orig]]
    
      predictions = predict_mpg(vehicle_config, model)
      return render_template('form.html',prediction_text="miles per gallon of car1,car2,car3={}".format(predictions)) 
    return render_template('form.html')





@app.route("/form1")
def form1():
    return render_template('form1.html')



@app.route("/predic", methods=['GET', 'POST'])
def predic():
    if request.method =='POST': 
      Cylinders = request.form['Cylinders']
      Cylinders= int(Cylinders)

      

      Displacement =request.form['Displacement']
      Displacement = int(Displacement)

      

      Horsepower =request.form['Horsepower']
      Horsepower = int(Horsepower)

      

      Weight = request.form['Weight']
      Weight = int(Weight)

      

      Acceleration =request.form['Acceleration']
      Acceleration = int(Acceleration)

      

      Model_Year = request.form['Model Year']
      Model_Year = int(Model_Year)

      
      Origin =request.form['Origin']
      Origin = int(Origin)
      
      if origin==3: 
          vehicle_config = [[Cylinders, 6,8 ], [Displacement,160,165],[Horsepower, 130, 98], [Weight,3150 , 2600], [Acceleration,14, 16], [Model_Year,80,78 ], [Origin,2 ,1]]
      elif origin==2:
          vehicle_config = [[Cylinders, 6,8 ], [Displacement,160,165],[Horsepower, 130, 98], [Weight,3150 , 2600], [Acceleration,14, 16], [Model_Year,80,78 ], [Origin,3 ,1]]
      elif origin==1:
          vehicle_config = [[Cylinders, 6,8 ], [Displacement,160,165],[Horsepower, 130, 98], [Weight,3150 , 2600], [Acceleration,14, 16], [Model_Year,80,78 ], [Origin,2 ,3]]
            
      predictions = predict_mpg(vehicle_config, model)
      a,b,c=predictions
      return render_template('form1.html',prediction_text="miles per gallon of car1={}".format(a)) 
    return render_template('form1.html')





@app.route("/form2")
def form2():
    return render_template('form2.html')



@app.route("/predi", methods=['GET', 'POST'])
def predi():
    if request.method =='POST': 
      Cylinders = request.form['Cylinders']
      Cylinders= int(Cylinders)

      Cylinder = request.form['Cylinder']
      Cylinder = int(Cylinder)

      

      Displacement =request.form['Displacement']
      Displacement = int(Displacement)

      Displacemen = request.form['Displacemen']
      Displacemen = int(Displacemen)

      

      Horsepower =request.form['Horsepower']
      Horsepower = int(Horsepower)

      Horsepowe =request.form['Horsepowe']
      Horsepowe = int(Horsepowe)

      

      Weight = request.form['Weight']
      Weight = int(Weight)

      Weigh = request.form['Weigh']
      Weigh = int(Weigh)

     

      Acceleration =request.form['Acceleration']
      Acceleration = int(Acceleration)

      Acceleratio = request.form['Acceleratio']
      Acceleratio = int(Acceleratio)

      

      Model_Year = request.form['Model Year']
      Model_Year = int(Model_Year)

      Model_Yea = request.form['Model Yea']
      Model_Yea = int(Model_Yea)

      
      
      Origin =request.form['Origin']
      Origin = int(Origin)
      
      Origi = request.form['Origi']
      Origi = int(Origi)
      
     
      vehicle_config = [[Cylinders, Cylinder,8 ], [Displacement, Displacemen, 165], [ Horsepower, Horsepowe, 98], [Weight, Weigh, 2600], [Acceleration, Acceleratio,16], [Model_Year, Model_Yea, 78], [Origin, Origi, 1]]
    
      a,b,c=predictions = predict_mpg(vehicle_config, model)
      return render_template('form2.html',prediction_text="miles per gallon of car1,car2={} and {}".format(a,b)) 
    return render_template('form2.html')
if __name__ == '__main__':
    app.run(debug=True)
