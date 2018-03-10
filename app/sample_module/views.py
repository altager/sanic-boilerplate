from app import jinja
from app.sample_module import sample_module


@sample_module.route('sample_module')
@jinja.template('sample_module/sample_page.html')
async def sample_page(requests):
    return
