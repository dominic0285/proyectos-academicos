<?php

function checkSpelling($text) {
    // Diccionario ampliado de palabras correctas en español
    $dictionary = [
    'hola', 'mundo', 'ejemplo', 'texto', 'correcto', 'verificar', 'palabra', 'ortografía',
    'programa', 'código', 'desarrollo', 'usuario', 'interfaz', 'biblioteca', 'archivo',
    'sistema', 'lenguaje', 'software', 'aplicación', 'computadora', 'internet', 'información',
    'proyecto', 'función', 'método', 'clase', 'objeto', 'variable', 'dato', 'algoritmo',
    'técnica', 'proceso', 'estrategia', 'análisis', 'sintaxis', 'error', 'resultado',
    'ejecutar', 'comprender', 'adquirir', 'configurar', 'instalar', 'redes', 'servidor',
    'cliente', 'base', 'datos', 'algoritmos', 'recursos', 'entorno', 'documentación',
    'funcionalidad', 'implementación', 'interacción', 'salida', 'entrada', 'control',
    'prototipo', 'interactivo', 'progresivo', 'tecnología', 'informático', 'desarrollador',
    'móvil', 'plataforma', 'hardware', 'red', 'sistema', 'virtual', 'nube', 'aplicaciones',
    'diseño', 'visual', 'proyecto', 'secuencia', 'prototipo', 'metodología', 'metodologías',
    'programación', 'algoritmo', 'parámetro', 'variable', 'funciones', 'clases', 'bucle',
    'iteración', 'estructura', 'condicional', 'proyecto', 'interfaz', 'navegador', 'usuario',
    'método', 'complejidad', 'lenguajes', 'script', 'framework', 'despliegue', 'interacción',
    'acceso', 'herramientas', 'recursos', 'búsqueda', 'optimizaciones', 'personalización',
    'base', 'consultas', 'servicios', 'tecnologías', 'desarrollo', 'soluciones', 'integración',
    'gestión', 'almacenamiento', 'modelo', 'contexto', 'módulo', 'referencia', 'parámetros',
    'solución', 'ejemplo', 'visualización', 'métricas', 'desempeño', 'evaluación', 'métricas',
    'análisis', 'pruebas', 'resultados', 'documentación', 'entorno', 'configuración',
    'interacción', 'interfaces', 'práctica', 'aplicación', 'funcionalidad', 'recursos', 
    'prototipo', 'optimización', 'tendencias', 'dinámica', 'programadores', 'metodologías', 
    'colaboración', 'proyectos', 'distribución', 'mantenimiento', 'sostenibilidad', 'código',
    'código', 'diseño', 'visualización', 'desempeño', 'test', 'especificaciones', 'trazabilidad',
    'programadores', 'creación', 'innovación', 'soluciones', 'iniciativas', 'evolución',
    'eficiencia', 'flexibilidad', 'personalización', 'experiencia', 'resultados', 'revisión',
    'plataformas', 'actualización', 'metodología', 'evaluación', 'interacciones', 'compañero'
];

    // Dividir el texto en palabras
    $words = explode(" ", strtolower($text));
    
    $errors = [];
    
    // Verificar cada palabra
    foreach ($words as $word) {
        $word = preg_replace('/[^a-záéíóúñü]/i', '', $word); // Eliminar caracteres especiales
        
        if (!in_array($word, $dictionary) && !empty($word)) {
            // Buscar sugerencias
            $suggestion = suggestWord($word, $dictionary);
            $errors[] = "$word (quizás quisiste decir: <b>$suggestion</b>)";
        }
    }

    if (empty($errors)) {
        return "No se encontraron errores ortográficos.";
    } else {
        return "Errores encontrados: " . implode(", ", $errors);
    }
}

function suggestWord($word, $dictionary) {
    $suggestion = '';
    $minDistance = -1;

    // Buscar la palabra más cercana en el diccionario
    foreach ($dictionary as $dictWord) {
        $distance = levenshtein($word, $dictWord);
        if ($distance < $minDistance || $minDistance == -1) {
            $minDistance = $distance;
            $suggestion = $dictWord;
        }
    }

    return $suggestion;
}
