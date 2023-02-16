<h1  align=center><font  size = 6>Predicting Solar Flares and Flare Area Classes</font></h1>

<p align="center">
    <img src="https://images.ctfassets.net/cnu0m8re1exe/1RiWk3i0ceklxImgCFDrTD/af90389b5fadb31b7142b9f98247f917/Untitled_design__54_.png?fm=jpg&fl=progressive&w=660&h=433&fit=fill" height=400  width=1000> 
</p>

<small>Picture Source:<a  href="https://images.ctfassets.net/cnu0m8re1exe/1RiWk3i0ceklxImgCFDrTD/af90389b5fadb31b7142b9f98247f917/Untitled_design__54_.png?fm=jpg&fl=progressive&w=660&h=433&fit=fill">ctfassets.net</a></small>

<br>

<h2>Statement</h2>

The purpose of this study is based on the available data, it was estimated numbers of the <i>solar flares</i> production in spesific region on sun in the following <i>24 hours (with classes)</i>. I made <i>multi-output neural network model</i> for the predict dependent variables. Accuracy can change due to parameters. Please let me know the best parameters.  You can run, modify and download your own model from codes. Accuracy can change due to parameters. Please let me know the best parameters.</p>

<br>  

<h2>Keywords</h2>

<ul>
	<li>Multi-Output</li>
	<li>Neural Networks</li>
	<li>Space</li>
	<li>Sun</li>
	<li>Classification</li>
	<li>Deep Learning</li>
</ul>  

<br>

<h2>Datasets</h2>

<p>Datasets are downloaded from <a href="https://archive.ics.uci.edu/ml/datasets/Solar+Flare">archive.ics.uci.edu</a> website. You can find the details of the datasets in that website and also in the <i>flare.names</i> named file. <i>flare.data1</i> dataset has <i>13 columns</i> and <i>323 rows without the header</i> and <i>flare.data2</i> dataset has <i>13 columns</i> and <i>1066 rows without the header</i>. The database contains 3 potential classes, one for the number of times a certain type of solar flare occured in a 24 hour period. Each instance represents captured features for 1 active region on the sun. The data are divided into two sections. The second section <i>(flare.data2)</i> has had much more error correction applied to the it, and has consequently been treated as more reliable. This informations had refered from  <a href="https://archive.ics.uci.edu/ml/datasets/Solar+Flare">archive.ics.uci.edu</a> website.</p>

<b>Attribute Information:</b>

<ol>
	<li>Code for class (modified Zurich class) (A,B,C,D,E,F,H)</li>
	<li>Code for largest spot size (X,R,S,A,H,K)</li>
	<li>Code for spot distribution (X,O,I,C)</li>  
	<li>Activity (1 = reduced, 2 = unchanged)</li>  
	<li>Evolution (1 = decay, 2 = no growth, 3 = growth)</li>  
	<li>Previous 24 hour flare activity code (1 = nothing as big as an M1, 2 = one M1, 3 = more activity than one M1)</li>  
	<li>Historically-complex (1 = Yes, 2 = No)</li>  
	<li>Did region become historically complex on this pass across the sun's disk (1 = yes, 2 = no)</li>  
	<li>Area (1 = small, 2 = large)</li>  
	<li>Area of the largest spot (1 = <=5, 2 = >5)</li>  
</ol>


<b>From all these predictors three classes of flares are predicted, which are represented in the last three columns.</b>  

11. <i>C-class flares</i> production by this region in the following 24 hours (common flares)
12. <i>M-class flares</i> production by this region in the following 24 hours (moderate flares)
13. <i>X-class flares</i> production by this region in the following 24 hours (severe flares)

<br>

<p>Donor:    

Gary Bradshaw: gbradshaw@clipr.colorado.EDU</p>

<br>

<h2>Predicting Number of the Flares in Region (with class)</h2>

<p>Please look at <a  href="https://github.com/doguilmak/Predicting-Solar-Flares-and-Flare-Area-Classes/blob/main/pred_solar_flare_class_ann.ipynb">pred_solar_flare_class_ann.ipynb</a> file to see more details about the structure. You can see the <i>multi-output model</i> structure on the below. It gets inputs as 9 independent variables and gives 3 outputs (C, M, X classes).</p>

<div align="center">
	<img width=700  height=700 src="https://raw.githubusercontent.com/doguilmak/Predicting-Solar-Flares-with-XGBoost-and-ANN/main/assets/model.png">
</div>

<p>Every class has different <i>dense layer</i> before the <i>output layer</i>. <code>c_output</code> has <i>32</i>, <code>m_output</code> has <i>64</i> and <code>x_output</code> has <i>16</i> neurons. <code>c_output</code> be retrived directly from <code>dense_3</code>, <code>m_output</code> be retrived directly from <code>dense_4</code> and <code>x_output</code> be retrived directly from <code>dense_5</code>. You can use the model model with loading <a  href="https://github.com/doguilmak/Predicting-Solar-Flares-and-Flare-Area-Classes/blob/main/my_model.h5">my_model.h5</a> or you can use the whole model <a  href="https://github.com/doguilmak/Predicting-Solar-Flares-and-Flare-Area-Classes/tree/main/my_model">here</a>.</p>

<br>

<h2>Predicting Flare Classes</h2>

| C Class Flares Model Accuracy | M Class Flares Model Accuracy | X Class Flares Model Accuracy |
|--|--|--|
| <img src="https://raw.githubusercontent.com/doguilmak/Predicting-Solar-Flares-with-XGBoost-and-ANN/main/assets/C-Class_flares_model_accuracy.png"> | <img src="https://raw.githubusercontent.com/doguilmak/Predicting-Solar-Flares-with-XGBoost-and-ANN/main/assets/M-Class_flares_model_accuracy.png"> | <img src="https://raw.githubusercontent.com/doguilmak/Predicting-Solar-Flares-with-XGBoost-and-ANN/main/assets/X-Class_flares_model_accuracy.png"> |
| XGBoost Accuracy score: 0.897196261682243 | XGBoost Accuracy score: 0.8785046728971962 | XGBoost Accuracy score: 0.9906542056074766 | 

<br>

<h2>Contact Me</h2>

<p>If you have something to say to me please contact me:</p>  

<ul>
	<li>Twitter: <a  href="https://twitter.com/Doguilmak">Doguilmak</a></li>
	<li>Mail address: doguilmak@gmail.com</li>
</ul>
