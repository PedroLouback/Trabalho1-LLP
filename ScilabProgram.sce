clear
clc
i=1;
arq = readxls("FECHAMENTO_MAIS__NEGOCIADAS_5minutos.xls");
planilha = arq(1);
x=planilha.value; //foi passado apenas as células com valores para a váriavel x 
matriz=zeros(12,12); //foi criada uma matriz 12x12 composta de 0's
x(:,1)=[]; 
x(1,:)=[]; 
while i < 5
    x(6200,:)=[];
    i=i+1;
end //foi removidos os NaN
line1=1;
line2=12;
while line2 < 6200
    matriz = x(line1:line2,1:12);
    disp(matriz);
    disp(inv(matriz));
    mprintf("\n\n");
    line1=line1+1;
    line2=line2+1; 
end
