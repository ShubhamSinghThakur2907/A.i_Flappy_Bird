import 'package:flutter/material.dart';
import 'models/global.dart'  ;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
 
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);


  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  

   
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      color: Colors.yellow,
      home: SafeArea(
            child : DefaultTabController(
        length: 3,
        child: new Scaffold(
          body: Stack(
            children: <Widget>[
                TabBarView(
                  children: [
              new Container(
                color: darkGreyColor,
              ),
              new Container(
                color: Colors.orange,
                ),
              
              new Container(
                color: Colors.red,
              ),
                  ],
               ),
            
          Container(
            padding: EdgeInsets.only(left: 50),
            height: 160,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.only(
                bottomLeft: Radius.circular(50),
                bottomRight: Radius.circular(50) ), 
                color: Colors.white, 
            ),
            child:Row (
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: <Widget>[
                Text("Intray", style: intrayTitleStyle), 
                Container()
              ],),
            ),
            Container(
              height: 80 ,
              width: 80 ,
              margin: EdgeInsets.only(top: 120 , left: MediaQuery.of(context).size.width*0.5 -40 ),
            child: FloatingActionButton(
              child: Icon(Icons.add, size: 50,),
              backgroundColor: Colors.red,

              onPressed: null)
            )
            ],

             ),
          appBar: new TabBar(
            tabs: [
              
              Tab(
                icon: new Icon(Icons.rss_feed),
              ),
              Tab(
                icon: new Icon(Icons.perm_identity),
              ),
              Tab(icon: new Icon(Icons.settings),)
            ],
            labelColor: Colors.pink[200],
            unselectedLabelColor: Colors.grey,
            indicatorSize: TabBarIndicatorSize.label,
            indicatorPadding: EdgeInsets.all(5.0),
            indicatorColor: Colors.pink ,         ),
          backgroundColor: Colors.white,
        ),
      ),
    )
    );
    
  }
}
