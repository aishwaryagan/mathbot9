# Ontario Grade 9 Mathematics (MTH1W) Curriculum Expectations
# Based on the Ontario Mathematics Curriculum, Grades 9 and 10, 2005 (revised)

GRADE9_EXPECTATIONS = {
    "Mathematical Thinking": {
        "emoji": "🧠",
        "color": "#00d2ff",
        "expectations": [
            "MTT1.1 - Apply problem-solving strategies to investigate mathematical ideas",
            "MTT1.2 - Develop and apply reasoning skills to make mathematical conjectures",
            "MTT1.3 - Communicate mathematical thinking using precise language and notation",
            "MTT1.4 - Connect mathematical ideas to real-world contexts",
            "MTT1.5 - Select and use appropriate tools and strategies to solve problems",
        ]
    },
    "Number": {
        "emoji": "🔢",
        "color": "#ff6b6b",
        "expectations": [
            "B1.1 - Represent, compare, and order rational numbers",
            "B1.2 - Perform operations with integers and rational numbers",
            "B1.3 - Apply exponent rules (product, quotient, power of a power)",
            "B1.4 - Express numbers in scientific notation and standard form",
            "B1.5 - Solve problems involving percentages, ratios, and rates",
            "B1.6 - Distinguish between exact values and approximate values",
        ]
    },
    "Algebra": {
        "emoji": "📐",
        "color": "#ffd93d",
        "expectations": [
            "A1.1 - Evaluate algebraic expressions for given values of variables",
            "A1.2 - Add and subtract polynomials with up to 2 variables",
            "A1.3 - Multiply a polynomial by a monomial",
            "A2.1 - Solve first-degree equations with rational coefficients",
            "A2.2 - Rearrange formulas involving multiple variables",
            "A2.3 - Solve and verify linear inequalities",
            "A3.1 - Identify linear and non-linear relations from tables and graphs",
            "A3.2 - Determine the slope of a line from graphs, tables, and equations",
            "A3.3 - Graph linear relations using slope and y-intercept",
            "A3.4 - Write equations of lines in various forms (y=mx+b, Ax+By+C=0)",
            "A3.5 - Solve systems of linear equations graphically",
        ]
    },
    "Data": {
        "emoji": "📊",
        "color": "#06ffa5",
        "expectations": [
            "D1.1 - Collect and organize categorical and numerical data",
            "D1.2 - Determine measures of central tendency (mean, median, mode)",
            "D1.3 - Determine measures of spread (range, interquartile range)",
            "D1.4 - Analyze and interpret data using various representations",
            "D1.5 - Compare two or more sets of data",
            "D2.1 - Determine theoretical probability of an event",
            "D2.2 - Determine experimental probability and compare to theoretical",
            "D2.3 - Solve problems involving independent and dependent events",
        ]
    },
    "Geometry & Measurement": {
        "emoji": "📏",
        "color": "#c77dff",
        "expectations": [
            "E1.1 - Verify and apply the Pythagorean theorem",
            "E1.2 - Solve problems using primary trigonometric ratios (SOH CAH TOA)",
            "E1.3 - Determine angles and sides in right triangles",
            "E2.1 - Determine the perimeter and area of composite 2D shapes",
            "E2.2 - Determine the surface area of prisms, cylinders, and composite 3D figures",
            "E2.3 - Determine the volume of prisms, cylinders, and composite 3D figures",
            "E2.4 - Solve problems involving similar triangles",
        ]
    },
    "Financial Literacy": {
        "emoji": "💰",
        "color": "#ff9a3c",
        "expectations": [
            "F1.1 - Describe and compare financial goals using mathematical language",
            "F1.2 - Analyse and describe the effects of financial decisions",
            "F1.3 - Calculate simple interest using I = Prt",
            "F1.4 - Calculate compound interest and compare to simple interest",
            "F1.5 - Solve problems involving taxes, tips, discounts, and commission",
            "F1.6 - Create and analyse budgets for personal financial goals",
            "F1.7 - Describe and compare various savings and investment options",
        ]
    }
}

GROWING_SUCCESS_LEVELS = {
    "Limited": {
        "range": "50-59%",
        "description": "The student shows limited understanding of the concept. Let's go back to basics and build a solid foundation! 🧱",
        "emoji": "🌱",
        "color": "#ff6b6b"
    },
    "Some": {
        "range": "60-69%",
        "description": "The student shows some understanding. You're on the right track — let's fill in those gaps! 🔍",
        "emoji": "🌿",
        "color": "#ffd93d"
    },
    "Considerable": {
        "range": "70-84%",
        "description": "The student shows considerable understanding. Great work — you've got a strong grasp of this! 💪",
        "emoji": "🌳",
        "color": "#06ffa5"
    },
    "Thorough": {
        "range": "85-100%",
        "description": "The student shows thorough and insightful understanding. Outstanding mastery! 🌟",
        "emoji": "⭐",
        "color": "#00d2ff"
    }
}

GROWING_SUCCESS_CATEGORIES = {
    "Knowledge & Understanding": "Demonstrates knowledge of facts, concepts, procedures, and mathematical conventions",
    "Thinking": "Uses planning, processing, and critical/creative thinking to investigate and solve problems",
    "Communication": "Expresses mathematical ideas clearly using proper notation, vocabulary, and representations",
    "Application": "Applies knowledge and skills to real-world and mathematical situations"
}

QUICK_PROMPTS = [
    {"text": "Solve a linear equation", "emoji": "⚖️", "strand": "Algebra"},
    {"text": "Explain slope & y-intercept", "emoji": "📈", "strand": "Algebra"},
    {"text": "Help with the Pythagorean theorem", "emoji": "📐", "strand": "Geometry"},
    {"text": "Explain probability", "emoji": "🎲", "strand": "Data"},
    {"text": "How does compound interest work?", "emoji": "💰", "strand": "Financial Literacy"},
    {"text": "What are exponent rules?", "emoji": "🔢", "strand": "Number"},
    {"text": "Help me with a word problem", "emoji": "📝", "strand": "Mathematical Thinking"},
    {"text": "Find the area of a shape", "emoji": "📏", "strand": "Geometry"},
]
