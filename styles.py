# Jet: 312F2F           (ireng)
# Tiffany Blue: 84DCCF  (ijo)
# Uranian Blue: A6D9F7  (biru muda)
# Columbia Blue: BCCCE0 (abu-abu muda)
# Brown: BF98A0         (abang muda)

STYLES = {
    # <main>
    "main": """
    background-color: #ffffff;
    color: #312F2F;
    font: 15px "Raleway";
    """,
    # <browse_button>
    "browse_button": """
    QPushButton{
        background-color: #a8a4a4;
        color: #312F2F;
        border: none;
        border-radius: 20px;
        font: 15px "Open Sans";
    }
    QPushButton:hover{
        background-color: #a6f2f7;
        color: #312F2F;
        border: 3px solid #84DCCF;
        border-radius: 20px;
        font: 15px "Open Sans";
    }
    QPushButton:pressed{
        background-color: #84DCCF;
        color: #312F2F;
        border: none;
        border-radius: 20px;
        font: 13px "Open Sans";
    }
    """,
    # <msrcr_button>
    "msrcr_button": """
    QPushButton{
        background-color: #f5a3a3;
        color: #312F2F;
        border: none;
        border-radius: 20px;
        font: 15px "Open Sans";
    }
    QPushButton:hover{
        background-color: #a6f2f7;
        color: #312F2F;
        border: 3px solid #84DCCF;
        border-radius: 20px;
        font: 15px "Open Sans";
    }
    QPushButton:pressed{
        background-color: #84DCCF;
        color: #312F2F;
        border: none;
        border-radius: 20px;
        font: 13px "Open Sans";
    }
    """,
    # <msrcp_button>
    "msrcp_button": """
    QPushButton{
        background-color: #f5a3a3;
        color: #312F2F;
        border: none;
        border-radius: 20px;
        font: 15px "Open Sans";
    }
    QPushButton:hover{
        background-color: #a6f2f7;
        color: #312F2F;
        border: 3px solid #84DCCF;
        border-radius: 20px;
        font: 15px "Open Sans";
    }
    QPushButton:pressed{
        background-color: #84DCCF;
        color: #312F2F;
        border: none;
        border-radius: 20px;
        font: 13px "Open Sans";
    }
    """,
    # <predict_button>
    "predict_button": """
    QPushButton{
        background-color: #f56d6d;
        color: #151D3B;
        border: none;
        border-radius: 20px;
        font: 15px "Open Sans";
    }
    QPushButton:hover{
        background-color: #a6f2f7;
        color: #151D3B;
        border: 3px solid #84DCCF;
        border-radius: 20px;
        font: 15px "Open Sans";
    }
    QPushButton:pressed{
        background-color: #84DCCF;
        color: #312F2F;
        border: none;
        border-radius: 20px;
        font: 13px "Open Sans";
    }
    """,
    # <display>
    "display": """
    QPlainTextEdit{
        background-color: #DFDFDE;
        color: #151D3B;
        border: none;
        border-radius: 5px;
        padding: 5px;
        font: 15px "Courier New";
    }
    """,
}