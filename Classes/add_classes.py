import os

if __name__ == "__main__":
    # Example list of your class IDs
    codes = [
        # متطلبات الجامعة
        {"name": "لغة انجليزية", "code": "UN 01", "prerequisites": "لا يوجد"},
        {"name": "حقوق الانسان", "code": "UN02", "prerequisites": "لا يوجد"},
        {"name": "حاسب آلي", "code": "UN03", "prerequisites": "لا يوجد"},
        {"name": "تاريخ وفلسفة العلوم", "code": "UN04", "prerequisites": "لا يوجد"},
        {"name": "ثقافة اسلامية", "code": "UN05", "prerequisites": "لا يوجد"},
        {"name": "مبادئ الادارة والمحاسبة", "code": "UN06", "prerequisites": "لا يوجد"},
        {
            "name": "مصادر الطاقة وتلوث البيئة",
            "code": "UN07",
            "prerequisites": "لا يوجد",
        },
        # متطلبات الكلية الإجبارية من العلوم الأساسية
        {"name": "كيمياء عامة (1)", "code": "CH101", "prerequisites": "لا يوجد"},
        {"name": "كيمياء عامة (2)", "code": "CH102", "prerequisites": "CH101"},
        {"name": "فيزياء عامة (1)", "code": "PH101", "prerequisites": "لا يوجد"},
        {"name": "فيزياء عامة (2)", "code": "PH102", "prerequisites": "PH101"},
        {"name": "رياضيات عامة (1)", "code": "MT103", "prerequisites": "لا يوجد"},
        {"name": "رياضيات عامة (2)", "code": "MT104", "prerequisites": "MT103"},
        # متطلبات الكلية من العلوم التطبيقية الاختيارية
        {
            "name": "تقسيم المملكة الحيوانية (لافقاريات) (1)",
            "code": "ZL101",
            "prerequisites": "لا يوجد",
        },
        {"name": "تقسيم مملكة نباتية", "code": "BT101", "prerequisites": "لا يوجد"},
        {"name": "مبادئ الجيوفيزياء", "code": "GP101", "prerequisites": "لا يوجد"},
        {
            "name": "جيوفيزياء تثاقلية ومغناطيسة",
            "code": "GP102",
            "prerequisites": "لا يوجد",
        },
        {
            "name": "كيمياء البترول والبتروكيماويات",
            "code": "CH309",
            "prerequisites": "لا يوجد",
        },
        {"name": "الجيومورفولوجيا", "code": "GE102", "prerequisites": "لا يوجد"},
        {
            "name": "الاستشعار من البعد ونظم المعلومات الجغرافية",
            "code": "GE302",
            "prerequisites": "لا يوجد",
        },
        {"name": "مخاطر جيوبيئية", "code": "GE209", "prerequisites": "لا يوجد"},
        {"name": "الجيولوجيا الطبيعية", "code": "GE107", "prerequisites": "لا يوجد"},
        {
            "name": "مصادر المياه وهيدروجيوكيمياء",
            "code": "GE304",
            "prerequisites": "لا يوجد",
        },
        {"name": "مقدمة في علوم البحار", "code": "MR101", "prerequisites": "لا يوجد"},
        {"name": "علم البحار والمحيطات", "code": "MR102", "prerequisites": "لا يوجد"},
        {"name": "مقدمة في علم الصخور", "code": "GE106", "prerequisites": "لا يوجد"},
        {"name": "إحصاء رياضي", "code": "MT131", "prerequisites": "لا يوجد"},
        {"name": "شكل ظاهري وأجنة", "code": "BT102", "prerequisites": "لا يوجد"},
        {"name": "بيئة نباتية", "code": "BT206", "prerequisites": "لا يوجد"},
        {
            "name": "كيمياء تحليلية وكروماتوجرافي",
            "code": "CH403",
            "prerequisites": "لا يوجد",
        },
        {"name": "كيمياء العناصر الممثلة", "code": "CH207", "prerequisites": "لا يوجد"},
        {"name": "نباتات اقتصادية وطبية", "code": "BT109", "prerequisites": "لا يوجد"},
        {"name": "كيمياء تحليل بالأجهزة", "code": "CH451", "prerequisites": "لا يوجد"},
        {"name": "علم الحفريات", "code": "GE105", "prerequisites": "لا يوجد"},
        {"name": "بيئة وفونا مصرية", "code": "ZL209", "prerequisites": "لا يوجد"},
        {"name": "جيولوجية مصر", "code": "GE321", "prerequisites": "لا يوجد"},
        {
            "name": "أساسيات علم الخلية والأنسجة والأجنة",
            "code": "ZL103",
            "prerequisites": "لا يوجد",
        },
        {"name": "أسس الكيمياء العضوية", "code": "CH204", "prerequisites": "لا يوجد"},
        {"name": "فيزياء حيوية", "code": "PH313", "prerequisites": "لا يوجد"},
        {"name": "علم البلورات والمعادن", "code": "GE103", "prerequisites": "لا يوجد"},
        {
            "name": "حيود الأشعة السينية وعلم البلورات",
            "code": "PH210",
            "prerequisites": "لا يوجد",
        },
        {"name": "تحليل عددي 1", "code": "MT313", "prerequisites": "لا يوجد"},
        {"name": "موجات", "code": "PH201", "prerequisites": "لا يوجد"},
        {"name": "جبر", "code": "MT101", "prerequisites": "لا يوجد"},
        {"name": "ميكانيكا عامة", "code": "MT105", "prerequisites": "لا يوجد"},
        {"name": "مبادئ البرمجة", "code": "MT162", "prerequisites": "لا يوجد"},
        {
            "name": "تقسيم المملكة الحيوانية (حبليات)",
            "code": "ZL104",
            "prerequisites": "لا يوجد",
        },
        {"name": "حيوان عام", "code": "ZL108", "prerequisites": "لا يوجد"},
        {
            "name": "مقدمة في علم المعادن والصخور",
            "code": "GE108",
            "prerequisites": "لا يوجد",
        },
        {"name": "ثروة بحرية", "code": "MR103", "prerequisites": "لا يوجد"},
        {"name": "بيولوجيا بحرية", "code": "MR104", "prerequisites": "لا يوجد"},
        # برنامج علوم الحاسب - متطلبات التخصص الإجبارية
        {
            "name": "جبر خطي وهندسة (1)",
            "code": "MT201",
            "prerequisites": "MT101, MT105",
        },
        {"name": "التحليل الرياضي (1)", "code": "MT206", "prerequisites": "MT104"},
        {"name": "مقدمة نظرية الاحتمالات", "code": "MT231", "prerequisites": "MT131"},
        {
            "name": "المعادلات التفاضلية العادية",
            "code": "MT210",
            "prerequisites": "MT104",
        },
        {"name": "لغة برمجة (1)", "code": "MT261", "prerequisites": "MT162"},
        {"name": "البرمجة الموجهة", "code": "MT263", "prerequisites": "MT261"},
        {"name": "جبر خطي وهندسة (2)", "code": "MT202", "prerequisites": "MT201"},
        {"name": "التحليل الرياضي (2)", "code": "MT215", "prerequisites": "MT206"},
        {"name": "الرياضيات المتقطعة", "code": "MT203", "prerequisites": "MT101"},
        {
            "name": "هياكل البيانات والخوارزميات",
            "code": "MT264",
            "prerequisites": "MT261",
        },
        {"name": "تنظيم الحاسب", "code": "MT265", "prerequisites": "لا يوجد"},
        {"name": "بناء الحاسب", "code": "MT362", "prerequisites": "MT265"},
        {"name": "رسومات الحاسب", "code": "MT363", "prerequisites": "MT262"},
        {"name": "تحليل وتصميم الخوارزميات", "code": "MT364", "prerequisites": "MT264"},
        {"name": "نظم قواعد البيانات", "code": "MT366", "prerequisites": "MT264"},
        {"name": "تحليل وتصميم النظم", "code": "MT368", "prerequisites": "لا يوجد"},
        {"name": "تطوير البرمجيات", "code": "MT380", "prerequisites": "MT263"},
        {"name": "نظم تشغيل الحاسب", "code": "MT365", "prerequisites": "MT364"},
        {"name": "تصميم قواعد البيانات", "code": "MT367", "prerequisites": "MT366"},
        {"name": "شبكات الحاسب", "code": "MT461", "prerequisites": "لا يوجد"},
        {"name": "الذكاء الإصطناعي", "code": "MT464", "prerequisites": "MT365, MT365"},
        {"name": "نظرية الأعداد", "code": "MT401", "prerequisites": "لا يوجد"},
        {"name": "نظرية التشفير", "code": "MT478", "prerequisites": "MT364, MT231"},
        {"name": "بحث ومقال", "code": "MT490", "prerequisites": "لا يوجد"},
        # برنامج علوم الحاسب - متطلبات التخصص الاختيارية
        {
            "name": "التحليل العددي (1)",
            "code": "MT313",
            "prerequisites": "MT210, MT104",
        },
        {
            "name": "الطرق الرياضية (1)",
            "code": "MT319",
            "prerequisites": "MT210, MT215",
        },
        {"name": "تنظيم و معالجة الملفات", "code": "MT369", "prerequisites": "MT264"},
        {"name": "معالجة الصور", "code": "MT387", "prerequisites": "MT261"},
        {"name": "الشبكات العصبية", "code": "MT375", "prerequisites": "MT364"},
        {"name": "نظرية الطوابير", "code": "MT379", "prerequisites": "MT231"},
        {"name": "الطرق الرياضية (2)", "code": "MT320", "prerequisites": "MT319"},
        {"name": "بحوث عمليات", "code": "MT388", "prerequisites": "لا يوجد"},
        {
            "name": "الأوتوماتيكية واللغات الشكلية",
            "code": "MT462",
            "prerequisites": "MT368",
        },
        {"name": "المحاكاة والنمذجة", "code": "MT476", "prerequisites": "MT364, MT231"},
        {"name": "نظم المعلومات", "code": "MT465", "prerequisites": "MT368, MT366"},
        {"name": "تصميم صفحات ويب", "code": "MT477", "prerequisites": "MT362"},
        {"name": "النظم الموزعة", "code": "MT473", "prerequisites": "MT365"},
        {"name": "رسومات الحاسب المتقدمة", "code": "MT469", "prerequisites": "MT363"},
        {
            "name": "موضوعات مختارة لعلوم الحاسب (1)",
            "code": "MT475",
            "prerequisites": "يحدد بالقسم",
        },
        {"name": "شبكات حاسب متقدمة", "code": "MT470", "prerequisites": "MT461"},
        {"name": "نظم تشغيل متقدم", "code": "MT471", "prerequisites": "MT365"},
        {"name": "الشبكات الذكية", "code": "MT480", "prerequisites": "MT461"},
        {"name": "تصميم لغات البرمجة", "code": "MT463", "prerequisites": "MT462"},
        {
            "name": "نظرية التحكم الأمثل (1)",
            "code": "MT420",
            "prerequisites": "MT215, MT210",
        },
        {"name": "تطبيقات الذكاء الاصطناعي", "code": "MT472", "prerequisites": "MT464"},
        {
            "name": "موضوعات مختارة في علوم الحاسب (2)",
            "code": "MT485",
            "prerequisites": "تحدد بالقسم",
        },
    ]

    output_dir = "University_Mind_Map"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for item in codes:
        name = item["name"]
        code = item["code"].replace(" ", "_")  # Filename-friendly
        raw_prereqs = item["prerequisites"]

        # Process prerequisites into Obsidian links
        # Handles "لا يوجد", "يحدد بالقسم", and comma-separated codes
        prereq_list = []
        if raw_prereqs not in ["لا يوجد", "يحدد بالقسم", "تحدد بالقسم"]:
            # Split by comma and clean spaces
            parts = [p.strip().replace(" ", "_") for p in raw_prereqs.split(",")]
            prereq_list = [f"[[{p}]]" for p in parts]

        filename = f"{code}.md"
        filepath = os.path.join(output_dir, filename)

        content = f"""---
aliases: ["{name}"]
code: "{item["code"]}"
tags: [course, university]
---

# {name} ({item["code"]})

## Prerequisites
{", ".join(prereq_list) if prereq_list else "None"}

## Notes
- 
"""

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"Generated {len(codes)} files in {output_dir}/")
