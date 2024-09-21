TiposdeMIME= {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}
Nombredelarchivo = input("Introduce el nombre del archivo porfavor: ").strip().lower()
if '.' in Nombredelarchivo:
    extension = Nombredelarchivo[Nombredelarchivo.rfind('.'):].lower()
else:
    extension = ""
TiposdeMIME = TiposdeMIME.get(extension, "application/octet-stream")
print(TiposdeMIME)