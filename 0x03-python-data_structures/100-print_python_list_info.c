#include <Python.h>
/**
 * print_python_list_info - function
 * @p: object
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t refCount = Py_REFCNT(p);
	PyObject *type = Py_TYPE(p);

	printf("Size of the list: %zd\n", size);
	printf("Reference count: %zd\n", refCount);
	printf("Type of the object: %s\n", Py_TYPE(p)->tp_name);
}
