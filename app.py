import streamlit as st
import pandas as pd
from io import BytesIO
import sys
from main import FlightCrewDeclaration

# Set page config
st.set_page_config(
    page_title="Flight Crew Declaration",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #1f77b4;
        text-align: center;
    }
    .upload-box {
        border: 2px dashed #1f77b4;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("# ✈️ Flight Crew Declaration Generator")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.markdown("### 📋 Hướng dẫn")
    st.markdown("""
    **Bước 1:** Upload file Excel  
    **Bước 2:** Kiểm tra dữ liệu  
    **Bước 3:** Tạo PDF  
    **Bước 4:** Download kết quả  
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Định dạng file Excel")
    st.markdown("""
    File phải có các cột:
    - A: DATE (Ngày bay)
    - B: FLT (Số hiệu chuyến bay)
    - C: TYPE (Loại máy bay)
    - D: REG (Mã đăng ký)
    - E: DEP (Sân bay xuất phát)
    - F: STD (Giờ cất cánh)
    - L: Crew (Danh sách tổ bay)
    """)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📁 Upload File Excel")
    uploaded_file = st.file_uploader(
        "Chọn file Excel (Daily Flight Schedule)",
        type=['xlsx', 'xls'],
        help="Định dạng: .xlsx hoặc .xls"
    )

# Process file
if uploaded_file is not None:
    try:
        # Save uploaded file temporarily
        temp_file = f"temp_{uploaded_file.name}"
        with open(temp_file, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success("✅ File uploaded successfully!")
        
        # Show file info
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📄 File Name", uploaded_file.name)
        with col2:
            st.metric("📦 File Size", f"{uploaded_file.size / 1024:.2f} KB")
        with col3:
            st.metric("⏰ Type", "Excel")
        
        st.markdown("---")
        
        # Load and display data preview
        st.markdown("### 📊 Preview Dữ Liệu")
        
        try:
            # Read Excel file for preview
            excel_file = pd.ExcelFile(temp_file)
            df = pd.read_excel(temp_file)
            
            st.markdown(f"**Sheet name:** {excel_file.sheet_names[0]}")
            st.markdown(f"**Total rows:** {len(df)}")
            
            # Show preview
            with st.expander("🔍 Xem chi tiết dữ liệu", expanded=True):
                st.dataframe(df.head(10), use_container_width=True)
            
        except Exception as e:
            st.warning(f"⚠️ Không thể preview dữ liệu: {str(e)}")
        
        st.markdown("---")
        
        # Generate PDF button
        st.markdown("### 📄 Tạo PDF")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            output_filename = st.text_input(
                "Nhập tên file PDF output:",
                value="General_Declaration.pdf",
                help="Tên file PDF sẽ được tạo"
            )
        
        with col2:
            st.write("")  # Spacing
            st.write("")
        
        # Generate PDF button
        if st.button("🚀 Tạo PDF", use_container_width=True):
            try:
                with st.spinner("⏳ Đang xử lý dữ liệu và tạo PDF..."):
                    # Create declaration
                    declaration = FlightCrewDeclaration(temp_file)
                    
                    # Generate PDF in memory
                    pdf_output = BytesIO()
                    declaration.generate_pdf_bytes(pdf_output)
                    pdf_output.seek(0)
                    
                    st.success("✅ PDF tạo thành công!")
                    
                    # Download button
                    st.download_button(
                        label="📥 Download PDF",
                        data=pdf_output,
                        file_name=output_filename,
                        mime="application/pdf",
                        use_container_width=True
                    )
                    
            except Exception as e:
                st.error(f"❌ Lỗi khi tạo PDF: {str(e)}")
                st.info("💡 Kiểm tra lại định dạng file Excel")
        
    except Exception as e:
        st.error(f"❌ Lỗi: {str(e)}")

else:
    # Show empty state
    st.markdown("""
    <div style='text-align: center; padding: 3rem;'>
        <h2>👈 Vui lòng upload file Excel để bắt đầu</h2>
        <p>File phải chứa dữ liệu lịch bay (Daily Flight Schedule)</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 1rem; color: #888;'>
    <small>🚀 Flight Crew Declaration Generator v1.0 | Made with ❤️ for aviation</small>
</div>
""", unsafe_allow_html=True)
