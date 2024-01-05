from django.views.generic import FormView
from .forms import HTMLConverterForm


class HTMLView(FormView):
    form_class = HTMLConverterForm
    template_name = 'html_converter/html_converter.html'

    @staticmethod
    def text_to_html(text, br, op):
        text = text.split('\r\n')
        if op == '3':
            return '<br>\n'.join([w for w in text])
        html = ''
        text_len = len(text)
        options = {
            '1': f'{br}\n%(text)s',
            '2': f' %(text)s'
        }
        template = options.get(op, '')
        for i in range(text_len):
            if i == 0:
                html += f'<p>{text[i]}'
            elif not text[i] and html.strip().endswith('</p>'):
                html += '\n'
            elif html.strip().endswith('</p>'):
                html += f'\n<p>{text[i]}'
            elif text[i]:
                html += template % {'text': text[i]}
            if i == text_len - 1:
                html += '</p>'
            elif not text[i] and not html.strip().endswith('</p>'):
                html += '</p>\n'

        return html

    def post(self, request, *args, **kwargs):
        form = HTMLConverterForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            html_data = self.text_to_html(cd.get('text'), cd.get('br'), cd.get('tab'))
            custom_request = self.request.POST.copy()
            custom_request.update({'html': html_data})
            form = HTMLConverterForm(custom_request)
            return self.render_to_response(context={'form': form})

        return self.render_to_response(context={'form': form})
