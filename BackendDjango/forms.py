from django import forms
from django.contrib import admin
from .models import Univallunos

# Formulario que se activa en el menú de administración de Django cuando se hace el CRUD a Univallunos
class UnivallunosAdminForm(forms.ModelForm):
    class Meta:
        model = Univallunos
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UnivallunosAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos 'tipoDocumento' y 'numeroDocumento' sean editables solo en la creación
        if self.instance and self.instance.pk:
            self.fields['tipoDocumento'].widget.attrs['readonly'] = True
            self.fields['numeroDocumento'].widget.attrs['readonly'] = True
            self.fields['codigoEstudiante'].widget.attrs['readonly'] = True
        # Hacer que el campo 'codigoEstudiante' sea opcional inicialmente
        self.fields['codigoEstudiante'].required = False

class UnivallunosAdmin(admin.ModelAdmin):
    form = UnivallunosAdminForm

    # Lista de campos para mostrar en el formulario de edición
    list_display = ('nombres', 'apellidos', 'esEstudiante', 'tipoDocumento', 'numeroDocumento', 'correo', 'codigoEstudiante')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        univalluno = self.get_object(request, object_id)
        # Si es un estudiante, habilita el campo 'codigoEstudiante'
        if univalluno and univalluno.esEstudiante:
            extra_context['show_codigoEstudiante'] = True
        else:
            extra_context['show_codigoEstudiante'] = False
        return super(UnivallunosAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        if obj.esEstudiante:
            # Si es un estudiante, el campo 'codigoEstudiante' debe estar presente
            obj.codigoEstudiante = form.cleaned_data['codigoEstudiante']
        else:
            # Si no es un estudiante, deshabilita el campo 'codigoEstudiante'
            obj.codigoEstudiante = None
        super(UnivallunosAdmin, self).save_model(request, obj, form, change)
