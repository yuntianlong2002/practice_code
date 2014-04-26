package com.example.ambient;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.Timer;
import java.util.TimerTask;

import com.jjoe64.graphview.BarGraphView;
import com.jjoe64.graphview.CustomLabelFormatter;
import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.GraphView.GraphViewData;
import com.jjoe64.graphview.GraphView.LegendAlign;
import com.jjoe64.graphview.GraphViewDataInterface;
import com.jjoe64.graphview.GraphViewSeries;
import com.jjoe64.graphview.GraphViewSeries.GraphViewSeriesStyle;
import com.jjoe64.graphview.LineGraphView;
import com.jjoe64.graphview.ValueDependentColor;

import android.graphics.Color;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.os.Handler;
import android.app.Activity;
import android.app.ListActivity;
import android.util.Log;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.SimpleAdapter;
import android.widget.TextView;

public class MainActivity extends Activity implements SensorEventListener{

	final String LOGTAG="Ambient";
	SensorManager mSensorManager;
	Sensor mLight;
	Sensor mProximity;
	GraphView graphView;
	GraphViewSeries exampleSeries2=null;
	
	//Control
	boolean start=false;//Controlled by the button
	boolean near=false;//Controlled by the proximity sensor
	
	long counter=0;
	float reading=0;
	float last_reading=-1;
	
	int idx=0;
	float[] reading_table=new float[10];
	
	ArrayList<Map<String, String>> list ;
	SimpleAdapter adapter;
	
	TextView initial_seq;
	TextView serect;
	String serect_seq;
	
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        Log.d("Ambient","Before setLayout");
        setContentView(R.layout.activity_main);
        list = new ArrayList<Map<String, String>>();
        
        Log.d("Ambient","Before sensor");
        
        mSensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);
        mLight = mSensorManager.getDefaultSensor(Sensor.TYPE_LIGHT);
        mSensorManager.registerListener(this, mLight, SensorManager.SENSOR_DELAY_FASTEST);
        mProximity = mSensorManager.getDefaultSensor(Sensor.TYPE_PROXIMITY);
        mSensorManager.registerListener(this, mProximity, SensorManager.SENSOR_DELAY_FASTEST);
        
        String[] from = { "name", "value" };
        int[] to = { R.id.text_history1, R.id.text_history2 };
        Log.d("Ambient","Before adapter");
        adapter = new SimpleAdapter(this, list,R.layout.entry2, from, to);
        ListView lv=(ListView)findViewById(R.id.listview);
        lv.setAdapter(adapter);
        
        final Handler handler = new Handler();
        Runnable runnable = new Runnable() {
        	   @Override
        	   public void run() {
        	      /* do what you need to do */
        		  if(start && near){ 
        			  append();
        			  counter += 1;
        		  }
        	      /* and here comes the "trick" */
        	      handler.postDelayed(this, 1000);
        	   }
        	};
        	
        	handler.postDelayed(runnable, 1000);
        	
        	initial_seq=(TextView)findViewById(R.id.textView1);
        	serect=(TextView)findViewById(R.id.textView2);
    }
    
    /*public void onStartClick(View v){
     	start=true;
     	initial_seq.setText("");
     	serect.setText("");
     	serect_seq="";
    }
    
    public void onStopClick(View v){
     	start=false;
    }*/

	protected void onResume() {
		super.onResume();
	}

	@Override
	public void onAccuracyChanged(Sensor arg0, int arg1) {
		
	}
	@Override
	public void onSensorChanged(SensorEvent event) {
		

		if(event.sensor.getType() == Sensor.TYPE_LIGHT){
			reading=event.values[0]/2;
			
			DateFormat dateFormat = new SimpleDateFormat("mm:ss");
			Date date = new Date();
			
			//list.add(putData(dateFormat.format(date), Float.toString(reading)));
			//adapter.notifyDataSetChanged();
		}
	}
	
	 private HashMap<String, String> putData(String name, String value) {
	        HashMap<String, String> item = new HashMap<String, String>();
	        item.put("name", name);
	        item.put("value", value);
	        return item;
	 }
	 
	 public void append(){
		 //if(exampleSeries2!=null){
		//	 exampleSeries2.appendData(new GraphViewData(counter, reading), true,100);
		 //}
		if(Math.abs(last_reading-reading)>0.4f && idx<10){
			reading_table[idx]=reading;
			idx++;
			last_reading=reading;
			String to_be_print="";
			for(int i=0;i<idx;i++){
				to_be_print=to_be_print+Double.toString(reading_table[i])+" ";
			}
			initial_seq.setText(to_be_print);
			
		}
		else if(idx>=10){
			for(int i=0;i<10;i++)
				if(Math.abs(reading_table[i]-reading)<1f){
					serect_seq=serect_seq+Integer.toString(i)+" ";   
					break;
				}
			serect.setText(serect_seq);
					
		}
			
		 
		list.add(putData(Long.toString(counter),Float.toString(reading)));
		adapter.notifyDataSetChanged();
	 }
}
