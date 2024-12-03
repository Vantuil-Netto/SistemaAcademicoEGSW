from django.contrib import admin
from .models import (
    UF, Cidade, Estudante, Professor, AreaDoSaber, InstituicaoEnsino, 
    Curso, Disciplina, Turno, Turma, Matricula, TipoAvaliacao, Avaliacao, 
    Frequencia, Ocorrencia
)

admin.site.register(UF)
admin.site.register(Cidade)
admin.site.register(Estudante)
admin.site.register(Professor)
admin.site.register(AreaDoSaber)
admin.site.register(InstituicaoEnsino)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Turno)
admin.site.register(Turma)
admin.site.register(Matricula)
admin.site.register(TipoAvaliacao)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)
