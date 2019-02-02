from SeleniumLibrary.locators import ElementFinder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from robot.libraries.BuiltIn import BuiltIn
from robot.utils import timestr_to_secs, secs_to_timestr, type_name


js_wait_for_primefaces = """
    return PrimeFaces.ajax.Queue.isEmpty();
"""

class pfElementFinder(ElementFinder):
    def __init__(self, timeout=30.0, error_on_timeout=False, enable_implicit_wait=True):
        super(pfElementFinder, self).__init__(self._selib)
        self.timeout = timeout
        self.error_on_timeout = error_on_timeout
        self.enable_implicit_wait = enable_implicit_wait

    def find(self, locator, tag=None, first_only=True, required=True,
             parent=None):
        timeout = self.timeout

        if self.enable_implicit_wait:
            try:
                WebDriverWait(self._selib._current_browser(), timeout, 0.2)\
                    .until(lambda x: self._selib._current_browser().execute_script(js_wait_for_primefaces))
            except TimeoutException:
                if self.error_on_timeout:
                    raise TimeoutException('Timed out waiting for ' +
                                           'PrimeFaces queue to empty ' +
                                           'after specified timeout.')

        elements = ElementFinder.find(self, locator, tag, first_only, required, parent)
        return elements
                
    @property
    def _selib(self):
        return BuiltIn().get_library_instance('SeleniumLibrary')

class PrimeFacesLibrary:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '0.0.1'

    def __init__(self,
                 timeout=30.0,
                 error_on_timeout=False,
                 enable_implicit_wait=True):
        """
        """

        self.timeout = timeout
        self.error_on_timeout = error_on_timeout
        self.enable_implicit_wait = enable_implicit_wait

        self._selib._element_finder = pfElementFinder(timeout,
                                                      error_on_timeout,
                                                      enable_implicit_wait)

    def enable_implicit_wait_for_primefaces(self, state=True):
        if not isinstance(state,bool):
            raise TypeError("state must be boolean, got %s instead."
                            % type_name(state))

        self._selib._element_finder.enable_implicit_wait = state

    def disable_implicit_wait_for_primefaces(self):
        self.enable_implicit_wait_for_primefaces(False)

    def get_implicit_wait_timeout(self):
        return secs_to_timestr(self.timeout)

    def set_implicit_wait_timeout(self, seconds):
        old_timeout = self.get_implicit_wait_timeout()
        self.timeout = timestr_to_secs(seconds)
        self._selib._element_finder.timeout = self.timeout
        return old_timeout

    def wait_for_primefaces(self, timeout=None, message=None):

        if timeout:
            timeoutSecs = timestr_to_secs(timeout)
        else:
            timeoutSecs = self.timeout

        errmsg = message or ('Timed out waiting for PrimeFaces queue ' +
                             'to empty after specified timeout.')

        try:
            WebDriverWait(self._selib._current_browser(), timeoutSecs, 0.2)\
                .until(lambda x: self._selib._current_browser().execute_script(js_wait_for_primefaces))
        except TimeoutException:
            if self.error_on_timeout:
                raise TimeoutException(errmsg)
        
    @property
    def _selib(self):
        return BuiltIn().get_library_instance('SeleniumLibrary')
