import os
import random
import json

def CreateCode(n):
    alp=[]
    for i in range(26):
        alp.append(chr(ord('A')+i))
    code=''
    for i in range(n):
        code+=random.choice(alp)
    return code

start_sol=r"""
\documentclass{exam}
\usepackage{multicol}
\usepackage{circuitikz}
\ctikzset{bipoles/length=0.8cm}
\printanswers
\begin{document}
\centering
{\bf \LARGE Basics Electrical Engineering - Exam}
\vspace{1cm} \hrule  \vspace{0.5cm}
Student name: \hfill Roll.no. \hfill Code: --code--
\vspace{0.5cm} \hrule \vspace{0.5cm}
\begin{multicols}{2}
\begin{questions}
"""

start=r"""
\documentclass{exam}
\usepackage{multicol}
\usepackage{circuitikz}
\ctikzset{bipoles/length=0.8cm}
%\printanswers
\begin{document}
\centering
{\bf \LARGE Basics Electrical Engineering - Exam}
\vspace{1cm} \hrule  \vspace{0.5cm}
Student name: \hfill Roll.no. \hfill Code: --code--
\vspace{0.5cm} \hrule \vspace{0.5cm}
\begin{multicols}{2}
\begin{questions}
"""
end=r"""
\end{questions}
\end{multicols}
\vspace{1cm}
\centering{*** All The Best ***}
\end{document}
"""

n=10
papers=3
for i in range(papers):
    code=CreateCode(n)
    
    exm=open("exam_"+code+".tex","w")
    exm.write(start.replace("--code--",code))
    
    exmsol=open("exam_sol_"+code+".tex","w")
    exmsol.write(start_sol.replace("--code--",code))
    
    sec=os.listdir('sections/') 
    random.shuffle(sec)
    for i in sec:
        exm.write("\section{"+i+"}")
        exmsol.write("\section{"+i+"}")
        
        con = os.listdir('sections/'+i+'/')
        for j in con:
            c_json=json.load(open('sections/'+i+'/'+j,'r'))
            q_list=c_json["questions"]
            q_selected= random.choice(q_list)
            q_text = open('questionbank/'+q_selected+'.tex','r').read()
            p_json = json.load(open('questionbank/'+q_selected+'.json','r'))
            pars = p_json["parameters"]
            vals = random.choice(p_json["values"])
            for idx in range(len(pars)):
                q_text = q_text.replace("--"+pars[idx]+"--",str(vals[idx]))
            exm.write(q_text)
            exmsol.write(q_text)
    exm.write(end)
    exmsol.write(end)
    exm.close()
    os.system('pdflatex exam_'+code+'.tex')
    os.system('del exam_'+code+'.log')
    os.system('del exam_'+code+'.aux')
    exmsol.close()
    os.system('pdflatex exam_sol_'+code+'.tex')
    os.system('del exam_sol_'+code+'.log')
    os.system('del exam_sol_'+code+'.aux')



#end
