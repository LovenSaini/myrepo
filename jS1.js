//document.getElementById("contact").style.color="red";
var abc=document.getElementById("bu1");

document.write("HELLO JS");
document.write();

alert("IS SOMETHING WRONG");
confirm("REALLY");
prompt("YES");
alert("ARE U SURE");
var tr=false;
function revealMessage(){
if(tr==false){
confirm("ARE U SURE");
document.getElementById("d1").style.display='block';
tr=true;
document.getElementById("bu1").innerHTML="<i><b>GREAT</b></i>";
document.getElementById("bu1").style.background="rgba(255,200,255,0.50)";
document.getElementById("p1").innerHTML="ITs DONE!"
}
else{alert("ALREADY DONE");}

}
alert("i thing itts done.");