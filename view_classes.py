import json


# List of the courses
codes = [
    # متطلبات الجامعة
    {"name": "رياضيات عامة (1)", "code": "MT103", "prerequisites": "لا يوجد"},
    {"name": "رياضيات عامة (2)", "code": "MT104", "prerequisites": "MT103"},
    # متطلبات الكلية من العلوم التطبيقية الاختيارية
    {"name": "إحصاء رياضي", "code": "MT131", "prerequisites": "لا يوجد"},
    {"name": "تحليل عددي 1", "code": "MT313", "prerequisites": "لا يوجد"},
    {"name": "جبر", "code": "MT101", "prerequisites": "لا يوجد"},
    {"name": "ميكانيكا عامة", "code": "MT105", "prerequisites": "لا يوجد"},
    {"name": "مبادئ البرمجة", "code": "MT162", "prerequisites": "لا يوجد"},
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


def generate_topological_canvas(course_list, output_name="Degree_Map.canvas"):
    nodes = []
    edges = []

    # Visual Layout Constants
    # The values are high because for visability
    node_w, node_h = 560, 200
    x_gap, y_gap = 640, 1600

    # 1. Map for easy lookup
    course_map = {item["code"].replace(" ", "_"): item for item in course_list}
    code_to_id = {
        item["code"].replace(" ", "_"): f"node_{i}"
        for i, item in enumerate(course_list)
    }

    # 2. Calculate Depth (The "Level" based on Prerequisites)
    depths = {}

    def get_depth(code):
        if code in depths:
            return depths[code]

        item = course_map.get(code)
        if not item or item["prerequisites"] in [
            "لا يوجد",
            "يحدد بالقسم",
            "تحدد بالقسم",
        ]:
            depths[code] = 0
            return 0

        # Split prereqs and find the max depth among them
        prereqs = [
            p.strip().replace(" ", "_") for p in item["prerequisites"].split(",")
        ]
        max_p_depth = max([get_depth(p) for p in prereqs if p in course_map] or [-1])

        depths[code] = max_p_depth + 1
        return depths[code]

    # Calculate depth for every course
    for item in course_list:
        get_depth(item["code"].replace(" ", "_"))

    # 3. Group by calculated depth
    rows = {}
    for code, depth in depths.items():
        rows.setdefault(depth, []).append(course_map[code])

    # 4. Create Nodes
    for row_idx, depth in enumerate(sorted(rows.keys())):
        for col_idx, item in enumerate(rows[depth]):
            clean_code = item["code"].replace(" ", "_")
            node_id = code_to_id[clean_code]

            nodes.append(
                {
                    "id": node_id,
                    "type": "file",
                    "file": f"University_Mind_Map/{item['name']}_{clean_code}.md",
                    "x": col_idx * (node_w + x_gap),
                    "y": row_idx * (node_h + y_gap),
                    "width": node_w,
                    "height": node_h,
                }
            )

    # 5. Create Edges
    for item in course_list:
        target_code = item["code"].replace(" ", "_")
        raw_prereqs = item["prerequisites"]
        if raw_prereqs not in ["لا يوجد", "يحدد بالقسم", "تحدد بالقسم"]:
            prereqs = [p.strip().replace(" ", "_") for p in raw_prereqs.split(",")]
            for p_code in prereqs:
                if p_code in code_to_id:
                    edges.append(
                        {
                            "id": f"edge_{p_code}_{target_code}",
                            "fromNode": code_to_id[p_code],
                            "fromSide": "bottom",
                            "toNode": code_to_id[target_code],
                            "toSide": "top",
                        }
                    )

    with open(output_name, "w", encoding="utf-8") as f:
        json.dump({"nodes": nodes, "edges": edges}, f, indent=4)

    print("Topological Canvas generated successfully.")


if __name__ == "__main__":
    generate_topological_canvas(codes)
