//I will use interface, lines, rectangles, circles, text are all drawable objects they share move and resize function
//And seaperate coordinate class, and a canvas class
//the line, circle ... function will call the low level function to to the draw

//The top level class and functions will be 

class Canvas{
    private:
        double x;
        double y;
        double width;
        double height;
        double resolutionx;
        double resolutiony;
        
    public:
    Canvas(){
        
    }
}


class Coordinate{
    private:
        double x;
        double y;
    public:
    Coordinate(double x,double y){
        
    }
}

class DrawableInterface{
    DrawableInterface(){
        
    }
    virtual move();
    virtual resize();
}

class Line : public DrawableInterface{
    private:
    Coordinate x;
    Coordinate y;
    public:
    Line(Coordinate x,Coordinate y){
        
    }
    //implementation for resize : translate the new length to Coordinates
    //and move: change the center point
}

class Circle : public DrawableInterface{
    private:
    Coordinate o;
    double r;
    public:
    Circle(Coordinate o,double r){
    }
    //implementation for resize:simply change the R
    //and move:simply change the o
    
}

class Rectangle : public DrawableInterface{
    private:
    Coordinate left;
    Coordinate right;
    public:
    Rectangle(Coordinate left,Coordinate right){
    }
    //implementation for resize : translate the new width and height to Coordinate
    //and move: move the center point
    
}

class Text : public DrawableInterface {
    private:
    public:
    Text(String txt, int size, bool bold, bool underline,Coordinate start){
    }
    //implementation for resize: change the font size
    //and move change the start point Coordinate
    
}


//The low level function will be using openGL api call to directly draw and remove point on the screen
draw(int x,int y){
    
}

remove(int x,int y){
    
}
