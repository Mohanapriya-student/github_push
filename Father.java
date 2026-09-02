//Father is the base class
class Father{
void job(){
System.out.println("Retired professor");
}
void  hobby(){
System.out.println("news paper TV watching");
}
void property(){
System.out.println("a house in native village");
}
}
class Daughter extends Father{
public static void main(String[] ar){
Father f1=new Father();
f1.job();
f1.hobby();
f1.property();
Daughter d=new Daughter();
d.job();
d.hobby();
d.property();
}
}