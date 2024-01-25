import streamlit as st
import scanpy as sc

st.set_page_config(
        page_title = "scRNA-seq Explorer",
        page_icon = ":Home:"
    )

def load_and_print_anndata(uploaded_file):
    # Load AnnData from the uploaded file
    adata = sc.read_h5ad(uploaded_file)

    # Print the first 5 rows
    st.write("First 5 rows of AnnData:")
    st.write(adata.obs.head())

def generate_toy_anndata():
    adata_ref = sc.datasets.pbmc3k_processed()
    adata = sc.datasets.pbmc68k_reduced()
    var_names = adata_ref.var_names.intersection(adata.var_names)
    adata_ref = adata_ref[:, var_names]
    adata = adata[:, var_names]
    return adata

def main():
    
    st.title("scRNA-seq Explorer")

    st.markdown("This tool is for a **standard single cell RNA-seq analysis** using [**scanpy**](https://scanpy.readthedocs.io/en/stable/).")
    st.markdown("The basics: Learn what is [anndata](https://anndata.readthedocs.io/en/latest/), the Annotated data.")
    st.image("img/anndata_schema.svg", caption="anndata schema", width=450)

   

    # Create a sidebar for navigation
    st.sidebar.title("scRNA-seq analysis")
    page = st.sidebar.radio("Select Option", ["Upload AnnData", "Toy AnnData Demo"])

    if page == "Upload AnnData":
        # File uploader
        uploaded_file = st.sidebar.file_uploader("Upload AnnData file (.h5ad)", type=["h5ad"])

        if uploaded_file is not None:
            # Display file details
            st.write("Uploaded file details:")
            st.write({"name": uploaded_file.name, "type": uploaded_file.type, "size": uploaded_file.size})

            # Load and print AnnData
            load_and_print_anndata(uploaded_file)

    elif page == "Toy AnnData Demo":
        # Generate toy AnnData for demo
        demo_adata = generate_toy_anndata()
        # Print the first 5 rows
        st.write("First 5 rows of AnnData:")
        st.write(demo_adata.obs.head())

if __name__ == "__main__":
    main()
