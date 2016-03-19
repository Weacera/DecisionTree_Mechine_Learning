'''
Created on Feb 11, 2016

@author: NAVE
'''
import csv
import cmath
import math
import random
import sys
import os
from tkinter.tix import COLUMN
from lib2to3.fixer_util import String
from _elementtree import Element
class node(object):
    def __init__(self):
        pass
        self.name=None
        self.node=[]
        self.prev=None
        self.otherinfo=None
        self.nodenumber=None
        self.codecount=None
        self.positive_count=None
        self.negative_count=None
    def add(self):
        node1=node()
        self.node.append(node1)
        node1.prev=self
        return node1
    def traverses(self,file,count):
        pass
        
        for i in self.node:
            pass
            i_count=0
            #print(i_count,count)
            while True:
                if i_count>=count:
                    break;
                #print("inside",i_count,count)
                i_count=i_count+1;
                
                file.write(" | ")
                
            try:
                try:
                    file.write(i.prev.name)
                except:
                    pass
               
                file.write(": ")
                
                file.write(i.otherinfo)
               
                file.write("\n")
                #file.write(" node of ")
                
            except:
                pass
            i.traverses(file,count+1)
        return;
    def traverses1(self,file,count,print_value):
        pass
        
        for i in self.node:
            pass
            i_count=0
            #print(i_count,count)
            while True:
                if i_count>=count:
                    break;
                #print("inside",i_count,count)
                i_count=i_count+1;
                
                file.write(" | ")
               
            try:
                s=""
                try:
                    file.write(i.prev.name)
                    s=i.prev.name
                except:
                    pass
                
                file.write(": ")
                
                file.write(i.otherinfo)
                
                file.write("\n")
                if print_value=="YES":
                    print(s,":",i.otherinfo)
                #file.write(" node of ")
                
            except:
                pass
            i.traverses1(file,count+1,print_value)
        return;
    def calculate_accuracy(self,matrix,row,class_column,header_column):
        
        if(self.nodenumber==-1):
           #print(matrix[row,class_column])
           if(self.name==matrix[row,class_column]):
               return True
           else:
               return False
        else:
            #print(self.name)
            temp_name=self.name
            index=header_column.index(temp_name)
            #print(row,index)
            node_to_traverse=matrix[row,index]
            #print(matrix[row,index])
            for nodes_i in self.node:
                if nodes_i.otherinfo==node_to_traverse:
                    break;
            return_value=nodes_i.calculate_accuracy(matrix,row,class_column,header_column)
        return return_value
    def formstack(self,stack):
        pass
        if(self==None):
            return
        for i in self.node:
            i.formstack(stack)
            if i.nodenumber==-1:
               continue
            stack.append(i)
        return stack  
    def copytree(self,tree):
        if(tree==None):
            return
        for i in tree.node:
            tree1=self.add()
            tree1.name=i.name
            tree1.otherinfo=i.otherinfo
            tree1.nodenumber=int(i.nodenumber)
            tree1.positive_count=i.positive_count
            tree1.negative_count=i.negative_count
            tree1.copytree(i)

def formsub_matrix_pass_recursion(tree,head_row,matrix, training_rows, training_columns, training_rows_1, training_columns_1,header_column):
    dif_elements_1=[]
    elements_count_1={}
    elements_position_1={}
    element_location_1=0
    for i in training_rows_1:
        try:
            index_location=dif_elements_1.index(matrix[i,head_row])
            elements_position_1[index_location,elements_count_1[index_location,index_location]]=i
            elements_count_1[index_location,index_location]=elements_count_1[index_location,index_location]+1
        except:
            dif_elements_1.insert(element_location_1, matrix[i,head_row])
            elements_count_1[element_location_1,element_location_1]=1
            elements_position_1[element_location_1,0]=i
            element_location_1=element_location_1+1
    element_location_1=0
    for ii in dif_elements_1:
        total_count_of_element=elements_count_1[element_location_1,element_location_1]
        temp_matrix={}
        temp_row=0
        temp_col=0
        total_temp_mat_row=0
        total_temp_mat_col=0
        temp_matrix_row_location=[]
        temp_matrix_col_location=[]
        original_col_location=[]
        first_time_check=True
        temp_header_column=[]
        for jj in training_columns_1:
            if (jj==head_row):
                continue
            count_now_itteration=0
            temp_row=0
            temp_matrix_col_location.append(temp_col)
            original_col_location.append(jj)
            temp_header_column.append(header_column[jj])
            while True:
                temp_matrix[temp_row,temp_col]=matrix[elements_position_1[element_location_1,count_now_itteration],jj]
                total_temp_mat_row=temp_row
                total_temp_mat_col=temp_col
                if first_time_check:
                    temp_matrix_row_location.append(temp_row)
                temp_row=temp_row+1
                if count_now_itteration==(total_count_of_element-1):
                    break
                count_now_itteration=count_now_itteration+1
            temp_col=temp_col+1
            first_time_check=False
        element_location_1=element_location_1+1
        if len(original_col_location)>1:
            head_row_1,leaf_value,m_positive_count,m_negative_count=calculateentropy(temp_matrix, total_temp_mat_row+1, total_temp_mat_col+1, temp_matrix_row_location,temp_matrix_col_location,original_col_location)
            
            if leaf_value!=-1:
                tree1=tree.add()
                tree1.name=leaf_value
                tree1.otherinfo=ii
                tree1.nodenumber=-1
                tree1.positive_count=m_positive_count
                tree1.negative_count=m_negative_count
            else:
                tree1=tree.add()
                tree1.name=temp_header_column[head_row_1]
                
                tree1.otherinfo=ii
                tree1.nodenumber=head_row_1
                tree1.positive_count=m_positive_count
                tree1.negative_count=m_negative_count
                #print(tree1.name,tree1.positive_count,tree1.negative_count)
                formsub_matrix_pass_recursion(tree1,head_row_1, temp_matrix, total_temp_mat_row+1, total_temp_mat_col+1, temp_matrix_row_location, temp_matrix_col_location,temp_header_column)
def formsub_matrix_pass_recursion_new(tree,head_row,matrix, training_rows, training_columns, training_rows_1, training_columns_1,header_column):
    dif_elements_1=[]
    elements_count_1={}
    elements_position_1={}
    element_location_1=0
    for i in training_rows_1:
        try:
            index_location=dif_elements_1.index(matrix[i,head_row])
            elements_position_1[index_location,elements_count_1[index_location,index_location]]=i
            elements_count_1[index_location,index_location]=elements_count_1[index_location,index_location]+1
        except:
            dif_elements_1.insert(element_location_1, matrix[i,head_row])
            elements_count_1[element_location_1,element_location_1]=1
            elements_position_1[element_location_1,0]=i
            element_location_1=element_location_1+1
    element_location_1=0
    for ii in dif_elements_1:
        total_count_of_element=elements_count_1[element_location_1,element_location_1]
        temp_matrix={}
        temp_row=0
        temp_col=0
        total_temp_mat_row=0
        total_temp_mat_col=0
        temp_matrix_row_location=[]
        temp_matrix_col_location=[]
        original_col_location=[]
        first_time_check=True
        temp_header_column=[]
        for jj in training_columns_1:
            if (jj==head_row):
                continue
            count_now_itteration=0
            temp_row=0
            temp_matrix_col_location.append(temp_col)
            original_col_location.append(jj)
            temp_header_column.append(header_column[jj])
            while True:
                temp_matrix[temp_row,temp_col]=matrix[elements_position_1[element_location_1,count_now_itteration],jj]
                total_temp_mat_row=temp_row
                total_temp_mat_col=temp_col
                if first_time_check:
                    temp_matrix_row_location.append(temp_row)
                temp_row=temp_row+1
                if count_now_itteration==(total_count_of_element-1):
                    break
                count_now_itteration=count_now_itteration+1
            temp_col=temp_col+1
            first_time_check=False
        element_location_1=element_location_1+1
        if len(original_col_location)>1:
            head_row_1,leaf_value,m_positive_count,m_negative_count=calculateentropy_new(temp_matrix, total_temp_mat_row+1, total_temp_mat_col+1, temp_matrix_row_location,temp_matrix_col_location,original_col_location)
            
            if leaf_value!=-1:
                tree1=tree.add()
                tree1.name=leaf_value
                tree1.otherinfo=ii
                tree1.nodenumber=-1
                tree1.positive_count=m_positive_count
                tree1.negative_count=m_negative_count
            else:
                tree1=tree.add()
                tree1.name=temp_header_column[head_row_1]
                
                tree1.otherinfo=ii
                tree1.nodenumber=head_row_1
                tree1.positive_count=m_positive_count
                tree1.negative_count=m_negative_count
                #print(tree1.name,tree1.positive_count,tree1.negative_count)
                formsub_matrix_pass_recursion_new(tree1,head_row_1, temp_matrix, total_temp_mat_row+1, total_temp_mat_col+1, temp_matrix_row_location, temp_matrix_col_location,temp_header_column)

def prune(tree,matrix,rows,column,header_column,L,k,filename_1):
    tree_max=node()
    tree_max.name=tree.name
    tree_max.otherinfo=tree.otherinfo
    tree_max.nodenumber=tree.nodenumber
    tree_max.positive_count=tree.positive_count
    tree_max.negative_count=tree.negative_count
    tree_max.copytree(tree)
    L_count=0
    max_accuracy=calcuate_percentage(tree, matrix, rows, column, header_column)
    
    while True:
            
            stack_sample=[]
            count=1
            tree_sample=node()
            tree_sample.name=tree.name
            tree_sample.otherinfo=tree.otherinfo
            tree_sample.nodenumber=tree.nodenumber
            tree_sample.positive_count=tree.positive_count
            tree_sample.negative_count=tree.negative_count
            tree_sample.copytree(tree)
            try:
               M=random.randint(1,k)
            except:
               M=0
            M_count=0
            while True:
                stack_sample=[]
                stack_sample=tree_sample.formstack(stack_sample)
                #print(len(stack_sample))
                if(len(stack_sample)<=2):
                    break
                
                try:
                   N=random.randint(1,len(stack_sample)-1)
                except:
                   N=0
                if N==0:
                    break
                node_to_drop=stack_sample[N]
                #print(node_to_drop.name)
                node_to_drop_positive=node_to_drop.positive_count
                node_to_drop_negative=node_to_drop.negative_count
                previous_node=node_to_drop.prev
                newnode=previous_node.add()
                #print(node_to_drop_positive,node_to_drop_negative)
                if node_to_drop_positive > node_to_drop_negative:
                   newnode.name="1"
                else:
                   newnode.name="0"
                newnode.otherinfo=node_to_drop.otherinfo
                newnode.nodenumber=-1
                newnode.positive_count=node_to_drop_positive
                newnode.negative_count=0
                index=previous_node.node.index(node_to_drop)
                del previous_node.node[index]
                if M_count==M:
                    break
                M_count=M_count+1
            accuracy_now=calcuate_percentage(tree_sample, matrix, rows, column, header_column)
            #file = open(filename_1+str(L_count)+'I.dat', 'w+')
            #tree.traverses(file,0)
            if accuracy_now>max_accuracy:
                max_accuracy=accuracy_now
                tree_max=node()
                tree_max.name=tree_sample.name
                tree_max.otherinfo=tree_sample.otherinfo
                tree_max.nodenumber=tree_sample.nodenumber
                tree_max.positive_count=tree_sample.positive_count
                tree_max.negative_count=tree_sample.negative_count
                tree_max.copytree(tree_sample)
            if(L_count==L):
                break;
            L_count=L_count+1
            stack_sample=[]
            stack_sample=tree_sample.formstack(stack_sample)
            #print(len(stack_sample))
            
    return tree_max   
def calculatematrix(filename):
    pass
    training_set=[]
    training_output=[]
    detect_training_types=[]
    number_of_each_types=[]
    training_rows=[]
    training_cols=[]
    header_column=[]
    with open(filename,'r') as csvfile:
        documentread=csv.reader(csvfile)
        for row in documentread:
            training_set.append(row)
    loop_m1=training_set
    
    training_mat_col=len(training_set[0])
    training_mat_row=len(training_set)-1
    i_row=0;
    j_col=0;
    training_input={}
    while True:
        training_rows.append(i_row)
        while True:
            
            training_input[i_row,j_col]=(training_set[i_row+1][j_col])
            
            if i_row==0:
                training_cols.append(j_col)
                header_column.append(training_set[i_row][j_col])
            j_col=j_col+1
            
            if(j_col==training_mat_col):
                break
        j_col=0
        i_row=i_row+1
        if (i_row==training_mat_row):
            break
    return training_input,training_mat_row,training_mat_col,training_rows,training_cols,header_column

def calculateentropy(matrix,training_rows,training_columns,training_rows_1,training_cols_1,original_col_location):
    class_positive=0
    class_negative=0
    class_column=training_columns-1
    for i in training_rows_1:
        if(matrix[i,class_column]=='1'):
            class_positive=class_positive+1
        else:
            class_negative=class_negative+1
    if class_positive==training_rows:
       return -1,'1',class_positive,class_negative
    if class_negative==training_rows:
       return -1,'0',class_positive,class_negative
    if training_columns==2:
        #print("rows--------------------",training_rows)
        if class_positive >= class_negative:
            return -1,'1',class_positive,class_negative
        else:
            return -1,'0',class_positive,class_negative
    entropy_class_positive=(class_positive/training_rows)
    entropy_class_negative=(class_negative/training_rows)
    if entropy_class_positive==0:
        entropy_class_positive=1
    if entropy_class_negative==0:
        entropy_class_negative=1
    total_entropy=round(-(entropy_class_positive*math.log2(entropy_class_positive))-(entropy_class_negative*math.log2(entropy_class_negative)),6)
    max_gain=0
    max_col=0
    max_postive=0
    max_negative=0
    for i in training_cols_1:
        if i==class_column:
            continue
        dif_elements=[]
        elements_position={}
        elements_count={}
        elements_location=0
        for j in training_rows_1:
            try:
                index=dif_elements.index((matrix[j,i]))
                elements_position[index,elements_count[index,index]]=j
                elements_count[index,index]=elements_count[index,index]+1
            except:
                dif_elements.insert(elements_location,(matrix[j,i]))
                elements_count[elements_location,elements_location]=1
                elements_position[elements_location,0]=j
                elements_location=elements_location+1
        elements_location=0
        sum_for_elemenent=0
        for ii in dif_elements:
            total_count_of_element=elements_count[elements_location,elements_location]
            element_current_count=0
            element_positive=0
            while True:
                row_now=elements_position[elements_location,element_current_count]
                if matrix[row_now,class_column]=="1":
                    element_positive=element_positive+1
                if element_current_count==(total_count_of_element-1):
                    break
                element_current_count=element_current_count+1
            elements_location=elements_location+1
            positive_count_fraction=round(float(element_positive/total_count_of_element),6)
            element_negative=(total_count_of_element-element_positive)
            negative_count_fraction=round(float(element_negative/total_count_of_element),6)
            if positive_count_fraction==0:
                positive_count_fraction=1
            if negative_count_fraction==0:
                negative_count_fraction=1
            temp_calculation=round((-(positive_count_fraction*math.log2(positive_count_fraction))-(negative_count_fraction*math.log2(negative_count_fraction))),6)
            sum_for_elemenent=sum_for_elemenent+round((total_count_of_element/training_rows)*temp_calculation,6)
            #print(sum_for_elemenent)
          
        gain_now=round((total_entropy-sum_for_elemenent),6)
        
        if max_gain <= gain_now:
            max_gain=gain_now
            max_col=i
            max_postive=element_positive
            max_negative=element_negative
    #print("checking---",total_entropy,sum_for_elemenent,gain_now) 
    return max_col,-1,max_postive,max_negative
def calculateentropy_new(matrix,training_rows,training_columns,training_rows_1,training_cols_1,original_col_location):
    class_positive=0
    class_negative=0
    class_column=training_columns-1
    for i in training_rows_1:
        if(matrix[i,class_column]=='1'):
            class_positive=class_positive+1
        else:
            class_negative=class_negative+1
    if class_positive==training_rows:
       return -1,'1',class_positive,class_negative
    if class_negative==training_rows:
       return -1,'0',class_positive,class_negative
    if training_columns==2:
        #print("rows--------------------",training_rows)
        if class_positive >= class_negative:
            return -1,'1',class_positive,class_negative
        else:
            return -1,'0',class_positive,class_negative
    entropy_class_positive=float(class_positive/training_rows)
    entropy_class_negative=float(class_negative/training_rows)
    total_entropy=round(entropy_class_positive*entropy_class_negative,6)
    max_gain=0
    max_col=0
    max_postive=0
    max_negative=0
    for i in training_cols_1:
        if i==class_column:
            continue
        dif_elements=[]
        elements_position={}
        elements_count={}
        elements_location=0
        for j in training_rows_1:
            try:
                index=dif_elements.index((matrix[j,i]))
                elements_position[index,elements_count[index,index]]=j
                elements_count[index,index]=elements_count[index,index]+1
            except:
                dif_elements.insert(elements_location,(matrix[j,i]))
                elements_count[elements_location,elements_location]=1
                elements_position[elements_location,0]=j
                elements_location=elements_location+1
        elements_location=0
        sum_for_elemenent=0
        for ii in dif_elements:
            total_count_of_element=elements_count[elements_location,elements_location]
            element_current_count=0
            element_positive=0
            while True:
                row_now=elements_position[elements_location,element_current_count]
                if matrix[row_now,class_column]=="1":
                    element_positive=element_positive+1
                if element_current_count==(total_count_of_element-1):
                    break
                element_current_count=element_current_count+1
            elements_location=elements_location+1
            positive_count_fraction=round(float(element_positive/total_count_of_element),6)
            element_negative=(total_count_of_element-element_positive)
            negative_count_fraction=round(float(element_negative/total_count_of_element),6)
            if positive_count_fraction==0:
                positive_count_fraction=1
            if negative_count_fraction==0:
                negative_count_fraction=1
            temp_calculation=round((-(positive_count_fraction*negative_count_fraction)),6)
            sum_for_elemenent=sum_for_elemenent+round((total_count_of_element/training_rows)*temp_calculation,6)
            #print(sum_for_elemenent)
          
        gain_now=round((total_entropy-sum_for_elemenent),6)
        
        if max_gain <= gain_now:
            max_gain=gain_now
            max_col=i
            max_postive=element_positive
            max_negative=element_negative
    #print("checking---",total_entropy,sum_for_elemenent,gain_now) 
    return max_col,-1,max_postive,max_negative

def calcuate_percentage(tree,matrix,rows,column,header_column):
    pass
    count=0
    total_positive=0
    while True:
        return_value=tree.calculate_accuracy(matrix,count, column-1, header_column);
        if return_value==True:
            total_positive=total_positive+1
        if count==rows-1:
            break
        count=count+1
    return round((total_positive/rows)*100,2)
filename1=sys.argv[1]
filename2=sys.argv[2]
filename3=sys.argv[3]
L=int(sys.argv[4])
K=int(sys.argv[5])
print_Value=sys.argv[6]
training_input_1,training_rows,training_columns,training_rows_1,training_columns_1,header_column=calculatematrix(filename1)
#training_input_6,training_rows6,training_columns6,training_rows_6,training_columns_6,header_column6=calculatematrix(filename3)
training_input_2,training_rows2,training_columns2,training_rows_2,training_columns_2,header_column2=calculatematrix(filename2)
training_input_3,training_rows3,training_columns3,training_rows_3,training_columns_3,header_column3=calculatematrix(filename3)
head_row,leaf_value,m_positive_count,m_negative_count=calculateentropy(training_input_1, training_rows, training_columns, training_rows_1, training_columns_1,training_columns_1)
tree=node()
tree.name=header_column[head_row]
tree.nodenumber=int(head_row)
tree.positive_count=m_positive_count
tree.negative_count=m_negative_count
formsub_matrix_pass_recursion(tree,head_row,training_input_1, training_rows, training_columns, training_rows_1, training_columns_1,header_column)
file = open('ID3 before pruning.dat', 'w+')
#file.write(tree.name)
tree.traverses1(file,0,print_Value)
perentage=calcuate_percentage(tree, training_input_3, training_rows3, training_columns3, header_column3)

tree_new=prune(tree, training_input_2, training_rows2, training_columns2, header_column2, L, K,"ID3")
file_new = open('ID3 after pruning.dat', 'w+')
#file_new.write(tree_new.name)
tree_new.traverses1(file_new,0,print_Value)
perentage_p=calcuate_percentage(tree_new, training_input_3, training_rows3, training_columns3, header_column3)



head_rowz,leaf_valuez,m_positive_countz,m_negative_countz=calculateentropy_new(training_input_1, training_rows, training_columns, training_rows_1, training_columns_1,training_columns_1)
treez=node()
treez.name=header_column[head_row]
treez.nodenumber=int(head_row)
treez.positive_count=m_positive_count
treez.negative_count=m_negative_count
formsub_matrix_pass_recursion_new(treez,head_rowz,training_input_1, training_rows, training_columns, training_rows_1, training_columns_1,header_column)
filez = open('VARIENCE BEFORE PRUNING.dat', 'w+')
#filez.write(treez.name)
treez.traverses1(filez,0,print_Value)
perentagez=calcuate_percentage(treez, training_input_3, training_rows3, training_columns3, header_column3)

stack_sample=[]
stack_sample=treez.formstack(stack_sample)
tree_newz=prune(treez, training_input_2, training_rows2, training_columns2, header_column2, L, K,"VARIENCE")
filez_new = open('VARIENCE AFTER PRUNING.dat', 'w+')
#filez_new.write(tree_newz.name)
tree_newz.traverses1(filez_new,0,print_Value)
perentage_pz=calcuate_percentage(tree_newz, training_input_3, training_rows3, training_columns3, header_column3)
print("ID3 before pruning",perentage)
print("ID3 after pruning",perentage_p)
print("varience impurty before pruning",perentagez)
print("varience impurty after pruning",perentage_pz)