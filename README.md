
<h1 align="center">
  <span> VietHealth-GPT - Advancing Vietnamese HealthCare Assistant</span>
</h1>

This project aims to develop a Vietnamese Medical Foundation Assistant VietHealth-GPT.
## 💡 Get help - [Q&A](https://github.com/TranNhiem/Vietnamese_LLMs/discussions) or [Discord 💬](https://discord.gg/BC8Mqq8qYn)

<h3 align="center">
  <span> VietHealthGPT - Initialed Target Developments</span>
</h3>

<div align="center">
     <img width="auto" height="600px" src="./images/VietHealthGPT_medical_domains.png"/>
</div>

## VietHealth-GPT Demo: 
+ [**VietHealthGPT Instruct Version 2024-07**](http://140.115.53.104:6667/)

## 1. Roadmap Development of VietHealth-GPT: 

<div align="center">
     <img width="auto" height="500px" src="./images/VietHealth-GPT_Roadmap.png"/>
</div>

## Important Medical Benchmarks on Multiple Task -- Các Bộ Dữ Liệu Đánh Giá Quan Trọng: 

+ Comprehensive and Advanced Vietnamese Benchmark for Medical Language Model
  
Kho lưu trữ này bao gồm các bộ dữ liệu đánh giá chuẩn được thiết kế để đánh giá các mô hình trợ lý y tế. Dưới đây là mô tả chi tiết về từng bộ dữ liệu cùng với các chỉ số và kích thước mẫu của chúng.

| Danh Mục Đánh Giá         | Mô Tả Nhiệm Vụ Đánh Giá                                                                                    | Chỉ Số | Số Lượng Mẫu |
|--------------------------|------------------------------------------------------------------------------------------------------------|--------|--------------|
| **MedQA (USMLE)**        | 1273 câu hỏi thực tế từ kỳ thi cấp phép hành nghề y khoa Hoa Kỳ (USMLE). Các câu hỏi này kiểm tra kiến thức y khoa tổng quát, phản ánh các tình huống lâm sàng và kiến thức cơ bản cần thiết cho các bác sĩ. | ACC    | 1273          |
| **PubMedQA**             | 500 câu hỏi được xây dựng từ tiêu đề bài báo trên PubMed cùng với các bản tóm tắt làm ngữ cảnh. Bộ dữ liệu này kiểm tra sự hiểu biết và khả năng phân tích của các mô hình đối với nghiên cứu y sinh và tài liệu khoa học. | ACC    | 500           |
| **MedMCQA**              | 4183 câu hỏi từ các kỳ thi tuyển sinh y khoa ở Ấn Độ (AIIMS & NEET PG), bao gồm 2.4k chủ đề liên quan đến chăm sóc sức khỏe. Bộ dữ liệu này cung cấp cái nhìn sâu sắc về kiến thức y khoa từ bối cảnh giáo dục khác. | ACC    | 4183          |
| **MMLU-Kiến Thức Lâm Sàng** | 265 câu hỏi trắc nghiệm về kiến thức lâm sàng. Bộ dữ liệu này cung cấp các tình huống và câu hỏi liên quan đến các vấn đề y tế thực tế. | ACC    | 265           |
| **MMLU-Di Truyền Y Khoa**    | 100 câu hỏi trắc nghiệm về di truyền y học, tập trung vào các khía cạnh của di truyền học và các vấn đề liên quan đến gen. | ACC    | 100           |
| **MMLU-Giải Phẫu Học**     | 135 câu hỏi trắc nghiệm về giải phẫu học, kiểm tra kiến thức về cấu trúc cơ thể và chức năng của các hệ thống cơ thể. | ACC    | 135           |
| **MMLU-Y Học Chuyên Nghiệp** | 272 câu hỏi trắc nghiệm về y học chuyên nghiệp, tập trung vào các vấn đề liên quan đến thực hành y học chuyên sâu và kiến thức chuyên ngành. | ACC    | 272           |
| **MMLU-Sinh Học Đại Học** | 144 câu hỏi trắc nghiệm về sinh học cấp đại học, bao gồm các khái niệm sinh học cơ bản và nâng cao. | ACC    | 144           |
| **MMLU-Y Học Đại Học**     | 173 câu hỏi trắc nghiệm về y học cấp đại học, tập trung vào các kiến thức và kỹ năng cần thiết cho sinh viên y khoa. | ACC    | 173           |

## Chỉ Số Đánh Giá
Chỉ số Độ Chính Xác (ACC) được sử dụng làm chỉ số đánh giá chính trên tất cả các bộ dữ liệu. Đây là chỉ số quan trọng để đo lường mức độ chính xác và hiệu quả của các mô hình hỗ trợ y tế trong việc xử lý và
