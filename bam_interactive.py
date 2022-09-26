from bam import BAM
from bam_ui import BAM_UI


if __name__ == '__main__':
    # Establish dimensions of the symbols
    A_rows, A_columns, B_rows, B_columns = 6, 4, 3, 4
    #A_rows, A_columns, B_rows, B_columns = 10, 8, 7, 5
    
    bam = BAM(A_rows*A_columns, B_rows*B_columns) 
    
    BAM_UI(bam, A_rows, A_columns, B_rows, B_columns) 
