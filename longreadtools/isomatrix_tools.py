# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Isomatrix_tools.ipynb.

# %% auto 0
__all__ = ['isomatrix_to_anndata', 'download_test_data', 'simulate_isomatrix', 'simulate_and_save_isomatrices',
           'convert_and_save_file', 'multiple_isomatrix_conversion']

# %% ../nbs/Isomatrix_tools.ipynb 3
import pandas as pd
import scanpy as sc
from scanpy import AnnData
from scipy.sparse import csr_matrix
import warnings

def isomatrix_to_anndata(file_path:str,  # The path to the isomatrix csv file to be read.
                        sparse:bool=True  # Flag to determine if the output should be a sparse matrix.
) -> AnnData: # The converted isomatrix as a scanpy compatible  anndata object
    """
    This function converts an isomatrix txt file (SiCeLoRe output) into an AnnData object compatible with scanpy

    """
    
    # Read in the data from the file
    df = pd.read_csv(file_path, sep='\t', index_col=0)
    # Filter out rows where the transcriptId is "undef"
    df = df.loc[df["transcriptId"] != "undef"]
    
    df = df.reset_index()
    df = df.transpose()
    
    # Extract the rows with 'gene_id', 'transcript_id', 'nb_exons' from the DataFrame
    additional_info_rows = df.loc[df.index.intersection(['geneId', 'transcriptId', 'nbExons'])]
    # Drop 'gene_id', 'transcript_id', 'nb_exons' rows from the DataFrame if they exist
    df = df.drop(['geneId', 'transcriptId', 'nbExons'], errors='ignore')

    # Convert the DataFrame to a sparse matrix if the sparse flag is True
    if sparse:
        matrix = csr_matrix(df.values.astype('float32'))
    else:
        try:
            matrix = df.values.astype('float32')
        except ValueError:
            print("Error: Non-numeric data present in the DataFrame. Cannot convert to float.")
            return None
    
    # Convert the matrix to an AnnData object
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        anndata = sc.AnnData(X=matrix, obs=pd.DataFrame(index=df.index), var=pd.DataFrame(index=df.columns))
    
    # Add additional information to the AnnData object vars
    for info in ['geneId', 'transcriptId', 'nbExons']:
        if info in additional_info_rows.index:
            anndata.var[info] = additional_info_rows.loc[info, :].values
            if info == 'nbExons':
                anndata.var[info] = anndata.var[info].astype('int32')
    
    return anndata

# %% ../nbs/Isomatrix_tools.ipynb 4
def download_test_data() -> str: #The absolute path of the extracted file 'sample_isomatrix.txt' if the download is successful.
    """
    This function downloads a test data file from a specified URL, saves it locally, and extracts it.
    """
    import urllib.request
    import gzip
    import shutil
    import os

    # URL of the file to be downloaded
    url = "https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM3748nnn/GSM3748087/suppl/GSM3748087%5F190c.isoforms.matrix.txt.gz"

    # Download the file from `url` and save it locally under `file.txt.gz`:
    urllib.request.urlretrieve(url, 'file.txt.gz')

    # Check if the file is downloaded correctly
    if os.path.exists('file.txt.gz'):
        print("File downloaded successfully")
        # Now we need to extract the file
        with gzip.open('file.txt.gz', 'rb') as f_in:
            with open('sample_isomatrix.txt', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print("File extracted successfully")
        return os.path.abspath('sample_isomatrix.txt')
    else:
        print("Failed to download the file")
        return None


# %% ../nbs/Isomatrix_tools.ipynb 13
import numpy as np 
from pandas import DataFrame

def simulate_isomatrix(num_genes, # int, number of genes (groups of rows)
                       num_transcripts_per_gene, # int, number of transcripts per gene
                       num_samples, # int, number of samples (columns)
                       sparsity=0.95, # float, fraction of zeros in the data (default 0.95)
                       max_expression=100, # int, maximum expression level for any transcript in any sample
                       seed=0 # int, random seed for reproducibility
                      ) -> DataFrame : # DataFrame with simulated transcript expression data for demonstration purposes.
    """
    Simulate transcript expression data to match the structure of the first image provided by the user.
    Allows specifying the number of genes, transcripts per gene, and samples.
    """
    # Set random seed for reproducibility
    np.random.seed(seed)
    
    # Calculate total number of transcripts
    total_transcripts = num_genes * num_transcripts_per_gene
    
    # Generate random data
    data = np.random.rand(total_transcripts, num_samples)
    
    # Apply sparsity
    zero_mask = np.random.rand(total_transcripts, num_samples) > sparsity
    data[~zero_mask] = 0  # Set a fraction of data to 0 based on sparsity
    
    # Scale data to have values up to max_expression
    data = np.ceil(data * max_expression).astype(int)
    
    # Generate transcript and sample labels
    transcript_ids = [f"ENSMUST00000{str(i).zfill(6)}.1" for i in range(1, total_transcripts + 1)]
    gene_ids = [f"Gene_{(i // num_transcripts_per_gene) + 1}" for i in range(total_transcripts)]
    nb_exons = np.random.randint(1, 21, total_transcripts)  # Assuming 1-20 exons based on typical gene structures
    sample_ids = [f"CACCTACACGTCAAC{str(i).zfill(2)}" for i in range(1, num_samples + 1)]
    
    # Create DataFrame
    df = pd.DataFrame(data, index=gene_ids, columns=sample_ids)
    df.index.name = 'geneId'  # Add index name
    df.insert(0, 'transcriptId', transcript_ids)
    df.insert(1, 'nbExons', nb_exons)
    
    return df

import os




# %% ../nbs/Isomatrix_tools.ipynb 14
def simulate_and_save_isomatrices(num_isomatrix, # int, number of isomatrix to generate
                                num_genes, # int, number of genes (groups of rows)
                                num_transcripts_per_gene, # int, number of transcripts per gene
                                num_samples, # int, number of samples (columns)
                                sparsity=0.95, # float, fraction of zeros in the data (default 0.95)
                                max_expression=100, # int, maximum expression level for any transcript in any sample
                                seed=0, # int, random seed for reproducibility
                                output_dir='./', # str, directory to save the generated isomatrix txt files
                                return_paths=False # bool, return paths to the isomatrixs as a list of strings if True
                               ) -> list:
    """
    Simulate multiple isomatrix and save them as txt files in the specified directory.
    If return_paths is True, return a list of paths to the saved isomatrix files.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    output_files = []
    for i in range(num_isomatrix):
        # Generate isomatrix
        df = simulate_isomatrix(num_genes, num_transcripts_per_gene, num_samples, sparsity, max_expression, seed+i)
        
        # Save to txt file
        output_file = os.path.join(output_dir, f'isomatrix_{i+1}.txt')
        df.to_csv(output_file, sep='\t')
        
        print(f'Isomatrix {i+1} saved to {output_file}')
        output_files.append(output_file)
    
    if return_paths:
        return output_files

# %% ../nbs/Isomatrix_tools.ipynb 15
def convert_and_save_file(sample, verbose):
    anndata = isomatrix_to_anndata(sample)
    anndata.write_h5ad(sample.replace('.txt', '.h5ad'))
    if verbose:
        print(f"File {sample.replace('.txt', '.h5ad')} was successfully written to disk.")

# %% ../nbs/Isomatrix_tools.ipynb 16
from multiprocessing import Pool
import os
from functools import partial


def multiple_isomatrix_conversion(file_paths: list, # A list of file paths to be converted.
                                  verbose: bool = False # If True, print progress messages.
                                  ):
    """
    This function takes a list of file paths, converts each file from isomatrix to anndata format, 
    and saves the converted file in the same location with the same name but with a .h5ad extension.
    """
    with Pool() as p:
        p.map(partial(convert_and_save_file, verbose=verbose), file_paths)

